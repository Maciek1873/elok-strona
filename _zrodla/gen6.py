src = open('gen5.py').read().replace("exec(open('gen_loop.py').read())", "")
exec(src)
IC_AUTO=I('<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>');IC_WEB=I('<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18"/>');IC_SHOP=I('<path d="M5 8h14l-1.5 12h-11z"/><path d="M9 8a3 3 0 016 0"/>');IC_ADS=I('<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>')
def card(ic,name,amt,unit,desc,items,hot=False,badge=''):
    return ('<div class="pzc rv%s">%s<div class="top"><b>%s</b><i>%s</i></div><div class="am"><small>od</small><strong>%s</strong><span>%s</span></div><p>%s</p><ul>%s</ul>'
            '<a class="btn %s mag" href="konsultacja.html">Zapytaj o wycenę <span class="ar">→</span></a></div>')%(' hot' if hot else '',('<span class="badge">%s</span>'%badge) if badge else '',name,ic,amt,unit,desc,''.join('<li>%s%s</li>'%(CHK,x) for x in items),'pri' if hot else 'sec')
PZ=('<div class="pz">'
 +card(IC_AUTO,'Automatyzacje','600 zł','netto · jednorazowo','Pojedyncze automaty, panele, CRM, faktury i integracje.',['analiza Twojego procesu','wdrożenie i testy na Twoich danych','instrukcja dla zespołu','poprawki po starcie'],True,'Główna specjalizacja')
 +card(IC_WEB,'Strona internetowa','1 500 zł','netto · jednorazowo','Strona firmowa albo landing z formularzem wyceny.',['projekt i wykonanie','wersja na telefon','formularz z powiadomieniem','podstawy SEO i statystyki'])
 +card(IC_SHOP,'Sklep internetowy','2 500 zł','netto · jednorazowo','Płatności, wysyłki, połączenie z magazynem lub Allegro.',['karty produktów i koszyk','płatności i dostawy','połączenie z magazynem','szkolenie z obsługi'])
 +card(IC_ADS,'Kampanie reklamowe','700 zł','netto / mc + budżet reklam','Google, Facebook i Instagram, TikTok.',['plan i grupa klientów','teksty i grafiki reklam','poprawki co tydzień','raport co miesiąc'])
 +'</div>')
PT=ptable()
for k in ('cennik.html','index.html'):
    h,body=pages[k]; assert PT in body,k
    body=body.replace(PT,PZ if k=='cennik.html' else '<div class="pzmini">'+PZ+'</div>')
    if k=='cennik.html':
        a=body.index('<section class="band"><div class="wrap">'+shead('Co jest w cenie','W każdej usłudze <span class="g">w standardzie.</span>'));b=body.index('</section>',a)+10
        body=body[:a]+body[b:]
        body=body.replace('<section><div class="wrap">'+shead('Przykłady','Ile kosztują <span class="g">typowe projekty?</span>','Orientacyjne ceny startowe. Dokładną kwotę zawsze podajemy po rozmowie.'),'<section class="band"><div class="wrap">'+shead('Przykłady','Ile kosztują <span class="g">typowe projekty?</span>','Orientacyjne ceny startowe. Dokładną kwotę zawsze podajemy po rozmowie.'),1)
        body=body.replace('<section style="padding-top:0"><div class="wrap"><div class="promise rv">','<section><div class="wrap"><div class="promise rv">',1)
    pages[k]=(h,body)
h,body=pages['realizacja-sklep.html']
mk='<section class="band"><div class="wrap split"><div class="prose rv"><div class="eyebrow">Punkt wyjścia</div>'
assert mk in body
DEMO=('<section style="padding-top:0"><div class="wrap">'+shead('Demo','Wypróbuj panel <span class="g">samodzielnie.</span>','Przeklikaj zamówienia, oferty, klientów i dokumenty. Dane są przykładowe, nic się nie zepsuje.')
 +'<div class="demo rv"><div class="bar"><i></i><i></i><i></i><span>Panel sklepu · wersja demonstracyjna</span><a href="demo.html" target="_blank" rel="noopener">Otwórz na pełnym ekranie ↗</a></div><iframe src="demo.html" title="Demo panelu sklepu" loading="lazy"></iframe></div></div></section>')
body=body.replace(mk,DEMO+mk,1)
pages['realizacja-sklep.html']=(h,body)
exec(open('gen_loop.py').read())
