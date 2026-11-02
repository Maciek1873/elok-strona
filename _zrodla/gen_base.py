#!/usr/bin/env python3
# Generator podstron ELOK (prototyp). Wspólny nagłówek/stopka, osobne treści.
import os
OUT=os.path.dirname(os.path.abspath(__file__))+'/out'
os.makedirs(OUT,exist_ok=True)

FONTS='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,300..900;1,300..900&family=Figtree:wght@400;500;600&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">'

def head(title,desc,main=False):
    h='<meta charset="utf-8"><title>%s</title><meta name="description" content="%s"><meta name="claude:viewport-fit-sides" content="cover">%s<link rel="stylesheet" href="site.css">'%(title,desc,FONTS)
    if main: return h
    return '<!doctype html><html lang="pl"><head><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'+h+'</head><body>'

NAV='''<header class="nav" id="nav"><div class="wrap"><div class="bar">
<a class="logo" href="index.html">ELOK<span>.</span></a>
<div class="menu">
 <div class="dd"><button type="button">Usługi ▾</button><div class="panel">
  <a href="automatyzacje.html"><b>Automatyzacje i systemy</b><span>panele, integracje, procesy, które dzieją się same</span></a>
  <a href="strony.html"><b>Strony i sklepy</b><span>szybkie strony, które zbierają zapytania</span></a>
  <a href="marketing.html"><b>Marketing</b><span>Google, Meta i TikTok Ads</span></a></div></div>
 <a href="realizacje.html">Realizacje</a><a href="cennik.html">Cennik</a><a href="o-nas.html">O nas</a><a href="kontakt.html">Kontakt</a>
</div>
<a class="btn pri cta mag" href="kontakt.html">Bezpłatna konsultacja</a>
<button class="burger" id="burger" type="button" aria-label="Menu" aria-expanded="false"><i></i><i></i></button>
</div>
<div class="mob"><a href="automatyzacje.html">Automatyzacje</a><a href="strony.html">Strony i sklepy</a><a href="marketing.html">Marketing</a><a href="realizacje.html">Realizacje</a><a href="cennik.html">Cennik</a><a href="o-nas.html">O nas</a><a class="btn pri" href="kontakt.html">Bezpłatna konsultacja</a></div>
</div></header>'''

FOOT='''<div class="huge" aria-hidden="true">ELOK<span>.</span></div>
<footer><div class="wrap">
<div class="fgrid">
 <div><a class="logo" href="index.html" style="font-size:24px;padding:0">ELOK<span>.</span></a><p style="margin-top:14px;max-width:34ch">Automatyzacje, strony i marketing dla firm. Systemy szyte pod konkretny biznes.</p></div>
 <div><h4>Usługi</h4><a href="automatyzacje.html">Automatyzacje i systemy</a><a href="strony.html">Strony i sklepy</a><a href="marketing.html">Marketing</a><a href="cennik.html">Cennik</a></div>
 <div><h4>Firma</h4><a href="realizacje.html">Realizacje</a><a href="o-nas.html">O nas</a><a href="kontakt.html">Kontakt</a></div>
 <div><h4>Kontakt</h4><span style="display:block;color:var(--fg);font-weight:600;user-select:all">455 505 820</span><span style="display:block">pon–pt, 9–17</span><span style="display:block;margin-top:8px">elok-agency.pl</span></div>
</div>
<div class="fbot"><span>© 2026 ELOK · polska spółka · faktura VAT</span><span><a href="#" style="text-decoration:none">Polityka prywatności</a> · <a href="#" style="text-decoration:none">Regulamin</a> · <a href="#" style="text-decoration:none">Cookies</a></span></div>
</div></footer>
<script src="site.js"></script>'''

def form(title='Pokażemy, co da się <span class="g it">usprawnić u Ciebie.</span>',pre='o1'):
    ch=lambda i,n:'<label><input type="checkbox" id="%s"%s><span>%s</span></label>'%(i,' checked' if i==pre else '',n)
    return '''<section class="final" id="kontakt"><div class="wrap"><div class="box rv">
<div><div class="eyebrow">Bezpłatna konsultacja</div><h2 style="margin:22px 0 24px">%s</h2>
<p class="lead">Zostaw kontakt. Odezwiemy się w ciągu jednego dnia roboczego.</p>
<div class="perks"><div><i>✓</i>30 minut online, bez zobowiązań</div><div><i>✓</i>Konkretne pomysły dla Twojej branży</div><div><i>✓</i>Nawet jeśli nic nie zamówisz, zostajesz z planem</div></div>
<div class="phone">455 505 820<small>Wolisz zadzwonić? Pon–pt, 9–17</small></div></div>
<form class="f" novalidate>
<div><div style="font-size:14px;font-weight:600;margin-bottom:9px">Co Cię interesuje?</div><div class="opts">%s%s%s%s</div></div>
<label for="f-imie">Imię<input id="f-imie" autocomplete="given-name" placeholder="np. Marek" required></label>
<label for="f-kontakt">Telefon lub e-mail<input id="f-kontakt" autocomplete="tel" placeholder="np. 600 123 456" required></label>
<label for="f-opis">Co zabiera Ci najwięcej czasu?<textarea id="f-opis" placeholder="np. ręcznie przepisuję zamówienia z maili do systemu"></textarea></label>
<button class="btn pri mag" type="submit" style="justify-content:center">Umów konsultację <span class="ar">→</span></button>
<p class="note">Wysyłając, zgadzasz się na kontakt w sprawie konsultacji. Szczegóły w polityce prywatności.</p>
<div class="done"><b>Dziękujemy!</b>Odezwiemy się w ciągu jednego dnia roboczego.</div>
</form></div></div></section>'''%(title,ch('o1','Automatyzacja'),ch('o2','Strona lub sklep'),ch('o3','Marketing'),ch('o4','Jeszcze nie wiem'))

def phero(crumb,eyebrow,h1,lead,facts='',btns=True):
    b='<div class="btns" style="margin-top:34px"><a class="btn pri mag" href="#kontakt">Umów bezpłatną konsultację <span class="ar">→</span></a><a class="btn sec" href="cennik.html">Zobacz cennik</a></div>' if btns else ''
    return '<section class="phero"><div class="wrap"><div class="crumbs"><a href="index.html">ELOK</a> / %s</div><div class="eyebrow">%s</div><h1>%s</h1><p class="lead">%s</p>%s%s</div></section>'%(crumb,eyebrow,h1,lead,facts,b)

def faq(items):
    return '<div class="faq">'+''.join('<details><summary>%s</summary><p>%s</p></details>'%(q,a) for q,a in items)+'</div>'

def ico(k):
    P={'in':'<path d="M4 6h16v12H4z"/><path d="M4 7l8 6 8-6"/>','calc':'<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M8 7h8M8 11h2M12 11h2M8 15h2M12 15h2"/>','msg':'<path d="M4 5h16v11H9l-5 4z"/>','doc':'<path d="M6 3h9l4 4v14H6z"/><path d="M9 13l2 2 4-4"/>','box':'<path d="M3 7l9-4 9 4-9 4z"/><path d="M3 7v10l9 4 9-4V7"/>','cal':'<rect x="4" y="5" width="16" height="15" rx="2"/><path d="M4 10h16M9 3v4M15 3v4"/>','chart':'<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>','bank':'<path d="M3 10l9-6 9 6M5 10v8M10 10v8M14 10v8M19 10v8M3 20h18"/>','user':'<circle cx="12" cy="8" r="4"/><path d="M4 21c1-4 4-6 8-6s7 2 8 6"/>','link':'<path d="M10 14l4-4M8 11l-2 2a3 3 0 004 4l2-2M16 13l2-2a3 3 0 00-4-4l-2 2"/>','spark':'<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5L18 18M6 18l2.5-2.5M15.5 8.5L18 6"/>','bolt':'<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>','search':'<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/>','phone':'<rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 18h2"/>','shield':'<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/>','target':'<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="4"/><circle cx="12" cy="12" r="1"/>','layers':'<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>','pen':'<path d="M4 20l4-1 11-11-3-3L5 16z"/>'}
    return '<div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">%s</svg></div>'%P[k]

def feats(items,cls='grid3'):
    return '<div class="%s">'%cls+''.join('<div class="feat rv">%s<h3>%s</h3><p>%s</p>%s</div>'%(ico(k),t,d,('<span class="ex">%s</span>'%x) if x else '') for k,t,d,x in items)+'</div>'

def steps(items):
    return '<div class="steps"><div class="fill"></div>'+''.join('<div><span class="n">KROK %d</span><h3>%s</h3><p>%s</p></div>'%(i+1,t,d) for i,(t,d) in enumerate(items))+'</div>'

def shead(eyebrow,h2,lead=''):
    return '<div class="shead rv"><div><div class="eyebrow">%s</div><h2>%s</h2></div>%s</div>'%(eyebrow,h2,('<p class="lead">%s</p>'%lead) if lead else '')

STEPS=[('Konsultacja','30 minut online. Opowiadasz, jak pracujesz, my pokazujemy, co da się usprawnić.'),('Plan i wycena','Dostajesz projekt rozwiązania i konkretną cenę przed startem prac.'),('Budowa','Tworzymy system, stronę lub kampanię i testujemy na Twoich danych.'),('Start i rozwój','Uczymy zespół, wdrażamy i zostajemy, żeby rozwijać to dalej.')]

AUTO_BLOCK='''<div class="tabs" role="tablist" id="tabs" data-start="%d"></div>
<div class="stage" id="stage" role="tabpanel" aria-live="polite"></div>
<div class="idea rv"><div><b>Masz zupełnie inny pomysł?</b><p>To tylko przykłady. Opowiedz, co Ci zabiera czas, a zaprojektujemy rozwiązanie od zera.</p></div><a class="btn sec" href="#kontakt">Opowiedz o swoim procesie <span class="ar">→</span></a></div>'''

CASES='''<div class="cases">
<a class="case rv tilt" href="realizacja-serwis.html"><div class="glow"></div><span class="tag">Serwis samochodowy premium</span><h3>Od katalogu części do faktury bez przepisywania</h3><p>Części trafiają ze schematu w katalogu prosto do wyceny z aktualnymi cenami hurtowni. Klient dostaje ofertę online, a faktura powstaje jednym kliknięciem.</p><div class="flowmini"><span>katalog</span><span>wycena</span><span>mail</span><span>PDF</span><span>faktura</span></div><div class="kpi"><b>−87%</b><span>czasu na przygotowanie wycen</span></div><span class="link">Zobacz case study →</span></a>
<a class="case rv tilt" href="realizacja-panel.html"><div class="glow"></div><span class="tag">E-commerce · dwie marki</span><h3>Panel finansowy, który liczy sam</h3><p>Raporty kasowe, ofertowanie, analityka i osobne rozliczenie podatków dla każdej marki. Księgowość dostaje gotowe zestawienia.</p><div class="flowmini"><span>sprzedaż</span><span>raporty</span><span>podatki</span><span>księgowość</span></div><div class="kpi"><b>1</b><span>panel zamiast kilku programów i arkuszy</span></div><span class="link">Zobacz case study →</span></a>
</div>'''

WEB_ANIM='''<div class="dev rv"><div class="browser" aria-label="Animacja: strona buduje się od szkicu do gotowego projektu"><div class="tb"><i></i><i></i><i></i><span>twojafirma.pl</span></div>
<div class="site done" id="site"><div class="s-nav"><div class="blk s-logo"><span class="tx">TWOJA<span style="color:#B08A45">.</span></span></div><div class="s-links"><div class="blk"></div><div class="blk"></div><div class="blk"></div></div></div>
<div class="blk s-h1"><span class="tx">Fachowo. Szybko.</span></div><div class="blk s-h1b"><span class="tx" style="color:#9A7535">Bez czekania.</span></div>
<div class="blk s-p"><span class="tx">Wycenę dostajesz w kilka minut.</span></div><div class="blk s-p2"><span class="tx">Formularz działa całą dobę.</span></div>
<div class="blk s-btn"><span class="tx">Zamów wycenę →</span></div><div class="blk s-img"></div></div></div>
<div class="score" aria-label="Wynik szybkości strony"><svg viewBox="0 0 100 100"><circle cx="50" cy="50" r="44" fill="none" stroke="#28231A" stroke-width="7"/><circle id="ring" cx="50" cy="50" r="44" fill="none" stroke="#5BC48A" stroke-width="7" stroke-linecap="round" pathLength="100" stroke-dasharray="100" stroke-dashoffset="100"/></svg><b id="sc">98</b><small>SZYBKOŚĆ</small></div>
<div class="lead-pop" id="pop"><i>✓</i><div><b>Nowe zapytanie ze strony</b><span>trafiło do panelu i na telefon</span></div></div></div>'''

CHART='''<div class="chart rv" aria-label="Przykładowy wykres zapytań z reklam"><div class="hd"><span>ZAPYTANIA Z REKLAM · ILUSTRACJA</span><b>↗</b></div>
<svg viewBox="0 0 520 260"><defs><linearGradient id="ga" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#CFA85E" stop-opacity=".35"/><stop offset="1" stop-color="#CFA85E" stop-opacity="0"/></linearGradient><clipPath id="cl"><rect id="clr" x="0" y="0" width="520" height="260"/></clipPath></defs>
<g stroke="#28231A" stroke-width="1"><line x1="0" y1="60" x2="520" y2="60"/><line x1="0" y1="120" x2="520" y2="120"/><line x1="0" y1="180" x2="520" y2="180"/><line x1="0" y1="240" x2="520" y2="240"/></g>
<g clip-path="url(#cl)"><path d="M0 236 C60 230 90 226 130 214 S210 190 250 176 S340 130 390 104 S470 56 520 40 L520 240 L0 240Z" fill="url(#ga)"/><path d="M0 236 C60 230 90 226 130 214 S210 190 250 176 S340 130 390 104 S470 56 520 40" fill="none" stroke="#CFA85E" stroke-width="3.5" stroke-linecap="round"/><path d="M0 238 C80 236 150 232 220 226 S360 214 520 196" fill="none" stroke="#5E5747" stroke-width="2.5" stroke-dasharray="6 7"/></g></svg>
<div class="lg"><span><i style="background:#CFA85E"></i>reklamy + szybka strona + automatyczna obsługa</span><span><i style="background:#5E5747"></i>same reklamy</span></div></div>'''

def priceCards(mini=False):
    C=[('Automatyzacje','600','zł netto','wdrożenie','Pojedynczy automat lub integracja, np. przypomnienia SMS, raport na maila, połączenie dwóch programów.',['analiza procesu','wdrożenie i testy','instrukcja dla zespołu'],True,'automatyzacje.html'),
       ('Strona WWW','1 500','zł netto','jednorazowo','Szybka strona firmowa albo landing z formularzem wyceny, który trafia prosto do panelu.',['projekt i kodowanie','SEO i analityka','formularz z powiadomieniem'],False,'strony.html'),
       ('Sklep online','6 000','zł netto','jednorazowo','Sklep z płatnościami, wysyłką i połączeniem z magazynem lub marketplace.',['płatności i dostawy','integracje','szkolenie z obsługi'],False,'strony.html'),
       ('Marketing','700','zł netto / mc','+ budżet reklamowy','Prowadzenie kampanii Google, Meta lub TikTok z miesięcznym raportem wyników.',['strategia i kreacje','optymalizacja','raport co miesiąc'],False,'marketing.html')]
    out='<div class="prices">'
    for lab,am,cur,per,d,li,hot,href in C:
        out+='<div class="pc rv%s"><span class="lab">%s</span><div class="am"><small>od</small><b>%s</b><em>%s</em></div><span class="mono" style="font-size:12px;color:var(--dim)">%s</span>'%(' hot' if hot else '',lab,am,cur,per)
        if not mini: out+='<p>%s</p><ul>%s</ul>'%(d,''.join('<li>%s</li>'%x for x in li))
        out+='<a class="btn %s" href="%s">%s</a></div>'%('pri' if hot else 'sec',href,'Szczegóły →')
    return out+'</div>'

FAQ_MAIN=[('Czy muszę zmieniać programy, których używam?','Zwykle nie. Najczęściej łączymy to, co już masz: program do faktur, sklep, pocztę, kalendarz albo katalog. Nowy panel zbiera wszystko w jednym miejscu.'),
 ('Ile to kosztuje?','Ceny zaczynają się od 600 zł netto za automatyzację i 1 500 zł netto za stronę. Dokładną kwotę podajemy po konsultacji, przed startem prac.'),
 ('Czy to tylko dla dużych firm?','Nie. Najwięcej zyskują małe firmy, w których właściciel robi wszystko sam. Kilka prostych automatów oddaje mu godziny każdego dnia.'),
 ('Jak długo trwa wdrożenie?','To zależy od zakresu. Prosty automat to zwykle kilka dni, większy system lub sklep to kilka tygodni. Termin dostajesz razem z wyceną.'),
 ('Czy wystawiacie fakturę VAT?','Tak. ELOK to polska spółka, każda usługa jest na fakturę VAT.')]

