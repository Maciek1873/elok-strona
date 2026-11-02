#!/usr/bin/env python3
# Uruchamiać z katalogu v3: python3 gen4.py
src = open('gen3.py').read().replace("exec(open('gen_loop.py').read())", "")
exec(src)

CAR = '<svg viewBox="0 0 300 90" fill="none"><path d="M10 70 C10 58 20 52 36 50 L80 46 C96 30 116 20 150 19 L196 20 C222 22 240 34 256 46 L280 50 C292 53 296 60 296 70 L296 76 L10 76 Z" fill="#CFA85E" opacity=".9"/><path d="M92 46 C106 32 122 26 150 25 L192 26 C212 28 226 36 238 46 Z" fill="#17130D" opacity=".55"/><circle cx="70" cy="76" r="14" fill="#0B0A08"/><circle cx="70" cy="76" r="6" fill="#57492F"/><circle cx="238" cy="76" r="14" fill="#0B0A08"/><circle cx="238" cy="76" r="6" fill="#57492F"/></svg>'

WA_ANIM = '''<div class="wa rv" id="wa" aria-label="Animacja: strona się buduje, klient wysyła zapytanie, a powiadomienie trafia na telefon">
<div class="br"><div class="tb"><i></i><i></i><i></i><span>studionova.pl</span></div>
<div class="vp"><div class="pg">
 <div class="pn"><b>NOVA<span>.</span></b><em>Usługi · Cennik · Kontakt <u>Wycena</u></em></div>
 <div class="hr"><div><h6>Detailing, który <span>widać z daleka.</span></h6><p>Korekta lakieru, powłoki ceramiczne i pranie tapicerki. Wycena w kilka minut, termin nawet jutro.</p><span class="b">Zamów wycenę →</span></div><div class="im">''' + CAR + '''</div></div>
 <div class="sv"><div><b>Korekta lakieru</b><span>od 900 zł</span></div><div><b>Powłoka ceramiczna</b><span>od 1 500 zł</span></div><div><b>Pranie tapicerki</b><span>od 350 zł</span></div></div>
 <div class="fm"><h6>Zapytaj o wycenę. <span>Odpowiemy dziś.</span></h6><div class="f"><div class="in ph">Imię i nazwisko</div><div class="in ph">Telefon</div><div class="go">Zamów wycenę →</div></div></div>
</div><div class="sk"><i style="width:22%"></i><i style="width:70%;height:30px;margin-top:20px"></i><i style="width:52%;height:30px"></i><i style="width:60%"></i><i style="width:44%"></i><i style="width:26%;height:26px;margin-top:10px"></i></div></div></div>
<div class="ph"><div class="sc"><div class="clk">12:00</div><div class="dt">dzisiaj</div><div class="nt"><i>E<span>.</span></i><div><b>Nowe zapytanie ze strony</b><small>Marek Kowalski · 600 123 456 · trafiło do panelu</small></div></div></div></div>
<div class="score" aria-label="Wynik szybkości strony"><svg viewBox="0 0 100 100"><circle cx="50" cy="50" r="44" fill="none" stroke="#28231A" stroke-width="7"/><circle id="wring" cx="50" cy="50" r="44" fill="none" stroke="#5BC48A" stroke-width="7" stroke-linecap="round" pathLength="100" stroke-dasharray="100" stroke-dashoffset="100"/></svg><b id="wsc">0</b><small>SZYBKOŚĆ</small></div>
<div class="cur"><svg viewBox="0 0 24 32"><path d="M2 2 L2 26 L8 20 L12 30 L16 28 L12 18 L20 18 Z" fill="#fff" stroke="#111" stroke-width="2" stroke-linejoin="round"/></svg></div>
</div>'''

PART = '<svg viewBox="0 0 120 120"><circle cx="60" cy="60" r="44" fill="#C9C3B8"/><circle cx="60" cy="60" r="36" fill="#DDD8CF"/><circle cx="60" cy="60" r="14" fill="#9E978A"/><g fill="#B5AEA2">' + ''.join('<circle cx="%.1f" cy="%.1f" r="3.2"/>' % (60 + 24 * __import__('math').cos(a * 1.2566), 60 + 24 * __import__('math').sin(a * 1.2566)) for a in range(5)) + '</g><path d="M86 30 C104 44 108 74 92 92 L82 84 C94 70 92 48 78 38 Z" fill="#1A1712"/></svg>'

SHOPMOCK = '''<div class="shopmock" aria-label="Podgląd sklepu Tanie Oryginały"><div class="sb"><b>Tanie Oryginały</b><span>Szukaj po numerze części…</span></div>
<div class="pr"><div class="pimg">''' + PART + '''</div><div class="pinfo"><small>ORYGINAŁ BMW</small><h5>Tarcza hamulcowa przednia</h5><span class="oe">nr OE · 34 11 · · · · · ·</span><span class="av">Dostępna od ręki · wysyłka dziś</span><div class="pp">489 zł</div><div class="cart">Dodaj do koszyka</div></div></div>
<div class="toast"><i>✓</i>Zamówienie przyjęte · etykieta gotowa</div></div>'''

def cs(num, href, media, tag, h3, prob, did, kpi_b, kpi_s, video=False):
    vb = '<span class="playbadge"><i>▶</i>Film z działania</span>' if video else ''
    return ('<a class="cs rv" href="%s"><div class="media">%s%s</div><div class="txt"><div class="num"><b>CASE STUDY %s</b>%s</div><h3>%s</h3>'
            '<dl><div><dt>Problem</dt><dd>%s</dd></div><div><dt>Zrobiliśmy</dt><dd>%s</dd></div></dl>'
            '<div class="foot"><div class="kpi"><b>%s</b><span>%s</span></div><span class="go">Przeczytaj case study →</span></div></div></a>') % (href, media, vb, num, tag, h3, prob, did, kpi_b, kpi_s)

CS = ('<div class="cslist">'
 + cs('01', 'realizacja-serwis.html', '<img src="img/serwis.jpg" alt="Baza ofert w systemie serwisu samochodowego" loading="lazy">', 'Serwis samochodowy premium',
      'Od katalogu części do faktury bez przepisywania',
      'Wyceny powstawały ręcznie w kilku programach. Nawet 10 godzin tygodniowo.',
      'Jeden system: katalog części, ceny z hurtowni, oferta mailem i faktura jednym kliknięciem.',
      '−87%', 'czasu na przygotowanie wycen', True)
 + cs('02', 'realizacja-sklep.html', SHOPMOCK, 'Sklep internetowy · Tanie Oryginały',
      'Sklep, który sam pilnuje cen, stanów i dokumentów',
      'Ceny i dostępność trzeba było pilnować ręcznie, a każde zamówienie to kilka programów.',
      'Nowy sklep z panelem: ceny i stany z hurtowni co noc, wysyłki, paragony i faktury prawie bez klikania.',
      'co noc', 'ceny i stany całego katalogu aktualizują się same')
 + cs('03', 'realizacja-panel.html', '<img src="img/panel.jpg" alt="Panel finansowy z rozliczeniem dwóch firm" loading="lazy">', 'E-commerce · dwie marki',
      'Panel finansowy, który liczy sam',
      'Raporty kasowe ręcznie, oferty w osobnych programach, podatki liczone osobno dla dwóch marek.',
      'Jeden panel: raport kasowy, oferty, analityka i automatyczny podział podatków na marki.',
      '1', 'panel zamiast kilku programów i arkuszy')
 + '</div>')

def phonevid(src, poster, label):
    return ('<div class="phonevid rv"><video src="vid/%s" poster="img/%s" autoplay muted loop playsinline preload="metadata" aria-label="%s"></video>'
            '<button class="snd" type="button">🔈 Włącz dźwięk</button></div>') % (src, poster, label)

# ---------- podmiany w istniejących stronach ----------
for k in list(pages):
    h, body = pages[k]
    body = body.replace(CASES2, CS)
    pages[k] = (h, body)

h, body = pages['strony.html']
pages['strony.html'] = (h, body.replace(WEB_ANIM, WA_ANIM))

h, body = pages['index.html']
old = shead('Realizacje', 'Systemy, które <span class="g">już działają.</span>', 'Prawdziwe zrzuty ekranu z wdrożonych systemów. Kliknij, żeby przeczytać więcej.')
assert old in body
body = body.replace(old, shead('Case studies', 'Zobacz, <span class="g">co już zbudowaliśmy.</span>', 'Trzy prawdziwe wdrożenia. Przy każdym: jaki był problem, co zrobiliśmy i jaki jest efekt.'))
VIDSEC = ('<section class="band"><div class="wrap vidsplit"><div>' + phonevid('o-nas.mp4', 'p-o-nas.jpg', 'Film: poznaj ELOK') + '</div>'
          '<div class="rv"><div class="eyebrow">Poznaj nas w 40 sekund</div><h2 style="margin:12px 0 20px">Kim jesteśmy <span class="g">i co robimy.</span></h2>'
          '<p class="lead">Automatyzacje, strony i marketing. Każde rozwiązanie projektujemy pod konkretną firmę, bez gotowców.</p>'
          '<div class="btns" style="margin-top:30px"><a class="btn pri mag" href="konsultacja.html">Umów bezpłatną konsultację <span class="ar">→</span></a><a class="btn sec" href="o-nas.html">Więcej o nas</a></div></div></div></section>')
marker = '<section class="band"><div class="wrap">' + shead('Case studies', 'Zobacz, <span class="g">co już zbudowaliśmy.</span>', 'Trzy prawdziwe wdrożenia. Przy każdym: jaki był problem, co zrobiliśmy i jaki jest efekt.')
assert marker in body
body = body.replace(marker, VIDSEC + marker.replace('class="band"', '', 1), 1)
pages['index.html'] = (h, body)

h, body = pages['automatyzacje.html']
VID24 = ('<section class="band"><div class="wrap vidsplit"><div>' + phonevid('24h.mp4', 'p-24h.jpg', 'Film: firma, która pracuje całą dobę') + '</div>'
         '<div class="rv"><div class="eyebrow">Zobacz w 20 sekund</div><h2 style="margin:12px 0 20px">Firma, która pracuje, <span class="g">kiedy Ty śpisz.</span></h2>'
         '<p class="lead">Klient pyta o cenę o 23:47, a o 23:48 ma już ofertę. Rano czeka na Ciebie potwierdzone zamówienie. Tak działa dobrze ustawiona automatyzacja.</p></div></div></section>')
mk = '<section><div class="wrap narrow">' + shead('Pytania', 'Pytania o automatyzacje')
assert mk in body
body = body.replace(mk, VID24 + mk, 1)
pages['automatyzacje.html'] = (h, body)

h, body = pages['o-nas.html']
mk = '<section><div class="wrap">' + shead('Co nas wyróżnia', 'Cztery rzeczy, <span class="g">na które możesz liczyć.</span>')
assert mk in body
VIDON = ('<section><div class="wrap vidsplit"><div>' + phonevid('o-nas.mp4', 'p-o-nas.jpg', 'Film: poznaj ELOK') + '</div>'
         '<div class="rv"><div class="eyebrow">ELOK w 40 sekund</div><h2 style="margin:12px 0 20px">Tak o sobie <span class="g">mówimy.</span></h2>'
         '<p class="lead">Automatyzujemy to, co zabiera najwięcej czasu, budujemy strony, które zbierają zapytania, i wspieramy to marketingiem.</p></div></div></section>')
body = body.replace(mk, VIDON + mk.replace('<section>', '<section class="band">', 1), 1)
pages['o-nas.html'] = (h, body)

# ---------- CASE STUDIES (lista) ----------
pages['realizacje.html'] = (head('Case studies · ELOK', 'Case studies ELOK: wdrożenia automatyzacji, sklepów i paneli dla firm.'),
 phero('Case studies', 'Case studies', 'Wdrożenia, które <span class="g">pracują codziennie.</span>',
       'Prawdziwe firmy i prawdziwe systemy. Przy każdym case study opisujemy problem, rozwiązanie i efekt. Kliknij, żeby przeczytać całość.', btns=False)
 + '<section style="padding-top:0"><div class="wrap">' + CS
 + '<div class="callout rv" style="margin-top:30px"><div><b>Twoja firma może być następna</b><p>Opowiedz, jak pracujesz, a pokażemy, co da się usprawnić.</p></div><a class="btn pri mag" href="konsultacja.html">Umów konsultację <span class="ar">→</span></a></div></div></section>')

# ---------- CASE: SKLEP ----------
ORD = '''<div class="ordmock rv" aria-label="Podgląd panelu zamówień"><div class="h">Zamówienia · dziś<span>panel sklepu</span></div>
<div class="r"><b>#2481</b><span>Tarcze hamulcowe przód, 2 szt.</span><span class="st c">✓ Doręczone · paragon</span></div>
<div class="r"><b>#2482</b><span>Filtr oleju + uszczelka</span><span class="st b">Etykieta gotowa</span></div>
<div class="r"><b>#2483</b><span>Wycieraczki, komplet</span><span class="st a">Zamówione u dostawcy</span></div>
<div class="r"><b>#2484</b><span>Czujnik klocków hamulcowych</span><span class="st a">Zamówione u dostawcy</span></div></div>'''
pages['realizacja-sklep.html'] = (head('Case study: sklep Tanie Oryginały · ELOK', 'Sklep internetowy z oryginalnymi częściami BMW i MINI: ceny i stany z hurtowni, wysyłki i dokumenty automatycznie.'),
'''<section class="phero"><div class="wrap"><div class="crumbs"><a href="index.html">Strona główna</a> / <a href="realizacje.html">Case studies</a> / Tanie Oryginały</div><span class="tagbig" style="display:inline-flex;gap:10px;font-weight:700;font-size:15px;padding:8px 16px;border-radius:999px;background:rgba(207,168,94,.14);color:var(--gold)">Case study 02 · sklep internetowy</span><h1 style="max-width:18ch">Sklep, który sam pilnuje <span class="g">cen, stanów i dokumentów.</span></h1><p class="lead">Tanie Oryginały to sklep z oryginalnymi częściami BMW i MINI. Zbudowaliśmy go od zera, razem z panelem, który obsługuje zamówienia, wysyłki i księgowość.</p>
<div style="margin-top:26px"><a class="linkout" href="https://tanieoryginaly.pl" target="_blank" rel="noopener">Zobacz sklep na żywo: tanieoryginaly.pl ↗</a></div>
<div class="kpis"><div class="rv"><b>co noc</b><span>ceny i stany całego katalogu aktualizują się same</span></div><div class="rv"><b>1 panel</b><span>zamówienia, oferty, klienci, wysyłki i dokumenty</span></div><div class="rv"><b>1 klik</b><span>i etykieta kurierska drukuje się sama</span></div></div></div></section>
<section style="padding-top:0"><div class="wrap split"><div class="shot rv" style="position:relative;aspect-ratio:16/11">''' + SHOPMOCK + '''</div>''' + ORD + '''</div></section>
<section class="band"><div class="wrap split"><div class="prose rv"><div class="eyebrow">Punkt wyjścia</div><h2 style="margin:12px 0 22px">Dużo ręcznej pracy przy każdym zamówieniu.</h2>
<p>Stary sklep działał od lat na gotowej platformie. Ceny i dostępność części trzeba było pilnować ręcznie, a hurtownia zmienia je bardzo często.</p>
<p>Każde zamówienie oznaczało kilka programów: zamówienie u dostawcy, etykieta kurierska, paragon albo faktura i maile do klienta.</p></div>
<div class="ba rv" style="margin-top:0;grid-template-columns:1fr"><div class="bef"><h4>Przed</h4><ul><li>ręczne pilnowanie cen i stanów</li><li>zamówienia u dostawcy wpisywane osobno</li><li>etykiety i dokumenty robione ręcznie</li></ul></div><div class="aft"><h4>Po</h4><ul><li>ceny i stany z hurtowni co noc</li><li>zamówienie trafia prosto do panelu</li><li>etykieta, maile i dokumenty prawie same</li></ul></div></div></div></section>
<section><div class="wrap split"><div class="rv"><div class="eyebrow">Rozwiązanie</div><h2 style="margin:12px 0 10px">Od zamówienia <span class="g">do doręczenia.</span></h2>
<div class="tline"><div><b>Katalog z hurtowni</b><p>Co noc system sprawdza ceny i dostępność każdej części. Klient widzi aktualne dane, a strona ładuje się szybko.</p></div><div><b>Zamówienie w panelu</b><p>Każde zamówienie od razu trafia do panelu, gotowe do zamówienia u dostawcy.</p></div><div><b>Wysyłka jednym kliknięciem</b><p>Wpisujesz wagę, a etykieta kurierska drukuje się sama. Klient dostaje maile ze statusem przesyłki.</p></div><div><b>Dokumenty</b><p>Paragon albo faktura powstają automatycznie po doręczeniu, razem z dokumentem przyjęcia towaru.</p></div><div><b>Oferty i klienci</b><p>Oferta PDF na maila, a każdy klient ma w panelu historię zamówień i ofert.</p></div></div></div>
<div class="prose rv"><div class="eyebrow">Co dalej</div><h3 style="margin:12px 0 14px">System rośnie razem ze sklepem.</h3><p>Kolejne etapy to sprzedaż na Allegro z tego samego panelu i konta dla warsztatów partnerskich z indywidualnymi rabatami.</p>
<div class="tech" style="margin-top:24px"><span>WooCommerce</span><span>własna wtyczka</span><span>API hurtowni</span><span>InPost i DPD</span><span>wFirma</span><span>panel CRM</span></div></div></div></section>''')

# ---------- nazwa sekcji: Case studies ----------
for k in list(pages):
    h, body = pages[k]
    body = body.replace('>Realizacje</a>', '>Case studies</a>').replace("<div class=\"eyebrow\">Realizacje</div>", '<div class="eyebrow">Case studies</div>')
    body = body.replace('/ <a href="realizacje.html">Realizacje</a>', '/ <a href="realizacje.html">Case studies</a>')
    body = body.replace('>Zobacz realizacje</a>', '>Zobacz case studies</a>')
    pages[k] = (h, body)
NAV = NAV.replace('>Realizacje</a>', '>Case studies</a>')
FOOT = FOOT.replace('>Realizacje</a>', '>Case studies</a>')

exec(open('gen_loop.py').read())
