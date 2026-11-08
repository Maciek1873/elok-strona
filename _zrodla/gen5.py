#!/usr/bin/env python3
# Uruchamiać z katalogu v3: python3 gen5.py
src = open('gen4.py').read().replace("exec(open('gen_loop.py').read())", "")
exec(src)

def I(p, sw='2'):
    return '<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round">%s</svg>' % (sw, p)
CHK = I('<path d="M5 12.5l4.5 4.5L19 7"/>', '2.6')
PLAY = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M7 4.5v15l13-7.5z"/></svg>'
ARR = I('<path d="M5 12h14M13 6l6 6-6 6"/>')
SPK = I('<path d="M11 5L6 9H3v6h3l5 4z"/><path d="M15.5 8.5a5 5 0 010 7M18.5 5.5a9 9 0 010 13"/>')
UP = I('<path d="M12 19V5M6 11l6-6 6 6"/>')
CHEV = '<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="width:.8em;height:.8em;margin-left:4px"><path d="M6 9l6 6 6-6"/></svg>'
IG = I('<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".6" fill="currentColor"/>')
TT = '<svg class="ic" viewBox="0 0 24 24" fill="currentColor"><path d="M16.6 3c.3 2.2 1.6 3.6 3.9 3.8v3.1c-1.4.1-2.7-.3-3.9-1.1v6.3c0 3.9-3.2 6.4-6.8 5.8-2.6-.4-4.6-2.6-4.7-5.3-.2-3.5 2.8-6.4 6.4-5.9v3.3c-1.6-.5-3.2.6-3.2 2.3 0 1.4 1.1 2.4 2.4 2.4 1.4 0 2.4-1 2.4-2.6V3h3.5z"/></svg>'

# ---------- teaser case studies ----------
def ct(href, img, cat, cats, title, line, kb, ks, video=False):
    vb = '<span class="vb"><i>%s</i>Film z działania</span>' % PLAY if video else ''
    return ('<a class="ct rv" href="%s" data-c="%s"><div class="th"><img src="img/%s" alt="%s" loading="lazy">%s</div><div class="bd">'
            '<span class="tg">%s</span><h3>%s</h3><p>%s</p><div class="ft"><b>%s</b><span>%s</span><em>%s</em></div></div></a>') % (href, cats, img, title, vb, cat, title, line, kb, ks, ARR)

CT = ('<div class="cgrid">'
 + ct('realizacja-serwis.html', 'serwis.jpg', 'Automatyzacje · serwis samochodowy', 'auto panel', 'Od katalogu części do faktury bez przepisywania',
      'Wycena, oferta mailem i faktura w jednym systemie.', '−87%', 'czasu na wyceny', True)
 + ct('realizacja-sklep.html', 'sklep.jpg', 'Sklep internetowy · Tanie Oryginały', 'sklep auto', 'Sklep, który sam pilnuje cen, stanów i dokumentów',
      'Ceny z hurtowni co noc, wysyłki i dokumenty prawie bez klikania.', 'co noc', 'aktualne ceny i stany')
 + ct('realizacja-panel.html', 'panel.jpg', 'Panel firmowy · e-commerce', 'panel auto', 'Panel finansowy, który liczy sam',
      'Raporty kasowe, oferty i podatki dwóch marek w jednym miejscu.', '1 panel', 'zamiast kilku programów')
 + '</div>')

for k in list(pages):
    h, body = pages[k]
    body = body.replace(CS, CT)
    pages[k] = (h, body)

h, body = pages['realizacje.html']
body = body.replace('<section style="padding-top:0"><div class="wrap">' + CT,
    '<section style="padding-top:0"><div class="wrap"><div class="cfil" id="cfil"><button type="button" class="on" data-c="all">Wszystkie</button><button type="button" data-c="auto">Automatyzacje</button><button type="button" data-c="sklep">Sklepy</button><button type="button" data-c="panel">Panele i systemy</button></div>' + CT)
pages['realizacje.html'] = (h, body)

# ---------- telefon z filmem (nowa wersja) ----------
def phonevid2(src, poster, label):
    return ('<div class="phonevid rv"><video src="vid/%s" poster="img/%s" autoplay muted loop playsinline preload="metadata" aria-label="%s"></video>'
            '<button class="snd" type="button">%sWłącz dźwięk</button></div>') % (src, poster, label, SPK)
for k in list(pages):
    h, body = pages[k]
    body = body.replace(phonevid('o-nas.mp4', 'p-o-nas.jpg', 'Film: poznaj ELOK'), phonevid2('o-nas.mp4', 'p-o-nas.jpg', 'Film: poznaj ELOK'))
    pages[k] = (h, body)

h, body = pages['automatyzacje.html']
old = VID24
assert old in body
body = body.replace(old, '<section class="band"><div class="wrap vidsplit"><div>' + phonevid2('system.mp4', 'p-system.jpg', 'Film: prawdziwy system w serwisie') + '</div>'
    '<div class="rv"><div class="eyebrow">Zobacz w 27 sekund</div><h2 style="margin:12px 0 20px">Prawdziwy system <span class="g">w prawdziwym serwisie.</span></h2>'
    '<p class="lead">Katalog części, wycena z rabatem, oferta dla klienta i faktura. Bez przepisywania i bez przełączania się między programami.</p>'
    '<div class="btns" style="margin-top:28px"><a class="btn sec" href="realizacja-serwis.html">Przeczytaj case study <span class="ar">→</span></a></div></div></div></section>')
pages['automatyzacje.html'] = (h, body)

# ---------- nowa animacja strony ----------
WB = '''<div class="wb rv" id="wb" aria-label="Animacja: klient wysyła zapytanie ze strony, a powiadomienie trafia na telefon">
<div class="br"><div class="tb"><i></i><i></i><i></i><span>studionova.pl</span></div>
<div class="pg"><div class="pn"><b>NOVA<span>.</span></b><em>Usługi · Cennik · Kontakt</em></div>
<div class="hr"><div><h6>Detailing, który <span>widać z daleka.</span></h6><p>Korekta lakieru, powłoki ceramiczne i pranie tapicerki. Termin nawet jutro.</p><div class="tags"><span>Korekta lakieru</span><span>Ceramika</span><span>Tapicerka</span></div></div>
<div class="fm"><small>WYCENA W 24 H</small><b>Zapytaj o cenę</b><div class="in pl">Imię i nazwisko</div><div class="in pl">Telefon</div><div class="go">Wyślij zapytanie</div></div></div></div>
<div class="sk"><i style="width:18%"></i><i style="width:46%;height:26px;margin-top:22px"></i><i style="width:38%;height:26px"></i><i style="width:42%"></i><i style="width:30%"></i></div></div>
<div class="ph"><div class="sc"><div class="clk">12:00</div><div class="dt">dzisiaj</div><div class="nt"><i>E<span>.</span></i><div><b>Nowe zapytanie</b><small>Marek Kowalski, 600 123 456</small></div></div></div></div>
<div class="score" aria-label="Wynik szybkości strony"><svg viewBox="0 0 100 100"><circle cx="50" cy="50" r="44" fill="none" stroke="#28231A" stroke-width="7"/><circle id="wring" cx="50" cy="50" r="44" fill="none" stroke="#5BC48A" stroke-width="7" stroke-linecap="round" pathLength="100" stroke-dasharray="100" stroke-dashoffset="100"/></svg><b id="wsc">0</b><small>SZYBKOŚĆ</small></div>
<div class="cur"><svg viewBox="0 0 24 32"><path d="M2 2 L2 26 L8 20 L12 30 L16 28 L12 18 L20 18 Z" fill="#fff" stroke="#111" stroke-width="2" stroke-linejoin="round"/></svg></div></div>'''
h, body = pages['strony.html']
assert WA_ANIM in body
pages['strony.html'] = (h, body.replace(WA_ANIM, WB))

# ---------- cennik: co jest w cenie, przykłady, obietnice ----------
h, body = pages['cennik.html']
mk = '<section class="band"><div class="wrap">' + shead('Od czego zależy cena', 'Trzy rzeczy, które <span class="g">mają znaczenie.</span>')
assert mk in body
li = lambda xs: '<ul>' + ''.join('<li>%s%s</li>' % (CHK, x) for x in xs) + '</ul>'
EXTRA = ('<section class="band"><div class="wrap">' + shead('Co jest w cenie', 'W każdej usłudze <span class="g">w standardzie.</span>') + '<div class="incl">'
 + '<div class="rv"><h4>Automatyzacje</h4>' + li(['analiza Twojego procesu', 'wdrożenie i testy na Twoich danych', 'instrukcja dla zespołu', 'poprawki po starcie']) + '</div>'
 + '<div class="rv"><h4>Strona internetowa</h4>' + li(['projekt i wykonanie', 'wersja na telefon', 'formularz z powiadomieniem', 'podstawy SEO i statystyki']) + '</div>'
 + '<div class="rv"><h4>Sklep internetowy</h4>' + li(['płatności i dostawy', 'karty produktów i koszyk', 'połączenie z magazynem', 'szkolenie z obsługi']) + '</div>'
 + '<div class="rv"><h4>Kampanie reklamowe</h4>' + li(['plan i grupa klientów', 'teksty i grafiki reklam', 'poprawki co tydzień', 'raport co miesiąc']) + '</div>'
 + '</div></div></section>'
 + '<section><div class="wrap">' + shead('Przykłady', 'Ile kosztują <span class="g">typowe projekty?</span>', 'Orientacyjne ceny startowe. Dokładną kwotę zawsze podajemy po rozmowie.') + '<div class="exs rv">'
 + '<div><div><b>Przypomnienia SMS dla gabinetu</b><span>klient dostaje przypomnienie dzień przed wizytą</span></div><em>od 600 zł</em></div>'
 + '<div><div><b>Raport sprzedaży na maila co rano</b><span>dane z kilku programów w jednym zestawieniu</span></div><em>od 600 zł</em></div>'
 + '<div><div><b>Strona firmowa z formularzem wyceny</b><span>zapytania od razu w Twoim telefonie</span></div><em>od 800 zł</em></div>'
 + '<div><div><b>Sklep z płatnościami i wysyłką</b><span>gotowy do sprzedaży, ze szkoleniem</span></div><em>od 1 800 zł</em></div>'
 + '<div><div><b>Panel dla firmy: oferty, klienci, faktury</b><span>system szyty pod sposób, w jaki pracujesz</span></div><em>wycena po rozmowie</em></div>'
 + '</div></div></section>'
 + '<section style="padding-top:0"><div class="wrap"><div class="promise rv">'
 + '<div>' + I('<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 8h8M8 12h8M8 16h5"/>') + '<b>Cena przed startem</b><span>wiesz, ile zapłacisz, zanim zaczniemy</span></div>'
 + '<div>' + I('<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/>') + '<b>Faktura VAT</b><span>polska spółka, wszystko na fakturę</span></div>'
 + '<div>' + I('<path d="M4 6h16v12H4z"/><path d="M4 7l8 6 8-6"/>') + '<b>Bezpłatna konsultacja</b><span>30 minut, bez zobowiązań</span></div>'
 + '<div>' + I('<path d="M20 12a8 8 0 11-3-6.2"/><path d="M20 4v5h-5"/>') + '<b>Opieka po wdrożeniu</b><span>pomagamy i rozwijamy dalej</span></div>'
 + '</div></div></section>')
body = body.replace(mk, EXTRA + mk.replace('<section class="band">', '<section>', 1), 1)
pages['cennik.html'] = (h, body)

# ---------- stopka: social + do góry ----------
FOOT = FOOT.replace('<span class="m">odpowiadamy w 1 dzień roboczy</span></div>',
    '<span class="m">odpowiadamy w 1 dzień roboczy</span><div class="social"><a href="https://www.tiktok.com/@elok.agency" target="_blank" rel="noopener" aria-label="TikTok">' + TT + '</a><a href="https://www.instagram.com/elok.agency" target="_blank" rel="noopener" aria-label="Instagram">' + IG + '</a></div></div>', 1)
FOOT = FOOT.replace('<span><a href="#">Polityka prywatności</a> · <a href="#">Regulamin</a> · <a href="#">Cookies</a></span>',
    '<span><a href="#">Polityka prywatności</a> · <a href="#">Regulamin</a> · <a href="#">Cookies</a></span><button class="totop" type="button">Do góry ' + UP + '</button>', 1)
NAV = NAV.replace('Usługi ▾', 'Usługi' + CHEV)

# ---------- bez emoji / znaków: ✓ ▶ ▾ na ikony ----------
for k in list(pages):
    h, body = pages[k]
    body = body.replace('<span class="playbadge"><i>▶</i>', '<span class="playbadge"><i>' + PLAY + '</i>')
    body = body.replace('<b>▶</b>', '<b>' + PLAY + '</b>')
    body = body.replace('✓', CHK)
    pages[k] = (h, body)

exec(open('gen_loop.py').read())
