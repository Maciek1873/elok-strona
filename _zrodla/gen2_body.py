#!/usr/bin/env python3
exec(open('gen_base.py').read())

def svc_hero(cur,eyebrow,h1,lead,facts,vis,tint):
    tabs=''.join('<a href="%s"%s>%s</a>'%(h,' class="on"' if h==cur else '',n) for h,n in [('automatyzacje.html','Automatyzacje'),('strony.html','Strony i sklepy'),('marketing.html','Marketing')])
    return '''<section class="phero2" style="%s"><div class="wrap"><div>
<div class="crumbs"><a href="index.html">Strona główna</a> / Usługi / %s</div>
<span class="tagbig"><i></i>%s</span>
<h1>%s</h1><p class="lead">%s</p>%s
<div class="btns" style="margin-top:30px"><a class="btn pri mag" href="#kontakt">Umów bezpłatną konsultację <span class="ar">→</span></a><a class="btn sec" href="cennik.html">Zobacz cennik</a></div>
<div style="margin-top:34px"><div style="font-size:14.5px;color:var(--mut);margin-bottom:10px">Nasze usługi:</div><div class="sub-nav">%s</div></div>
</div><div class="vis rv">%s</div></div></section>'''%(tint,eyebrow,eyebrow,h1,lead,facts,tabs,vis)

AUTO_VIS='''<div class="auto-vis" aria-label="Przykład: zamówienie obsługuje się samo">
<div style="font-size:15px;color:var(--mut);margin-bottom:4px">Przykład: nowe zamówienie w sklepie</div>
<div class="r">%s<div><b>Przychodzi zamówienie</b><span>ze sklepu albo z Allegro</span></div><em>✓ samo</em></div>
<div class="r">%s<div><b>Magazyn się aktualizuje</b><span>wszędzie naraz</span></div><em>✓ samo</em></div>
<div class="r">%s<div><b>Klient dostaje SMS</b><span>z numerem paczki</span></div><em>✓ samo</em></div>
<div class="r">%s<div><b>Faktura idzie do KSeF</b><span>bez przepisywania</span></div><em>✓ samo</em></div>
<div class="ft"><span>Twoja praca przy tym zamówieniu</span><b>0 min</b></div></div>'''%(ico('in'),ico('box'),ico('msg'),ico('doc'))

def shot(src,cap,alt):
    return '<figure class="shot rv" style="margin:0"><img src="img/%s" alt="%s" loading="lazy"><figcaption>%s</figcaption></figure>'%(src,alt,cap)

CASES2='''<div class="cases">
<a class="case rv" href="realizacja-serwis.html"><div class="media"><img src="img/serwis.jpg" alt="Baza ofert w systemie dla serwisu samochodowego" loading="lazy"><span class="playbadge"><i>▶</i>Film z działania</span></div>
<div class="txt"><span class="tag">SERWIS SAMOCHODOWY PREMIUM</span><h3>Od katalogu części do faktury bez przepisywania</h3><p>Części z katalogu trafiają prosto do wyceny z aktualnymi cenami hurtowni. Faktura powstaje jednym kliknięciem.</p><div class="kpi"><b>−87%</b><span>czasu na przygotowanie wycen</span></div><span class="link">Zobacz realizację i film →</span></div></a>
<a class="case rv" href="realizacja-panel.html"><div class="media"><img src="img/panel.jpg" alt="Panel finansowy z rozliczeniem dwóch firm" loading="lazy"></div>
<div class="txt"><span class="tag">E-COMMERCE · DWIE MARKI</span><h3>Panel finansowy, który liczy sam</h3><p>Raporty kasowe, oferty, analityka i osobne rozliczenie podatków dla każdej marki.</p><div class="kpi"><b>1</b><span>panel zamiast kilku programów</span></div><span class="link">Zobacz realizację →</span></div></a>
</div>'''

PRICES=[('Automatyzacje i systemy','pojedyncze automaty, panele, CRM, faktury, integracje','od 600 zł','jednorazowo'),
 ('Strona internetowa','strona firmowa albo landing z formularzem','od 1 500 zł','jednorazowo'),
 ('Sklep internetowy','płatności, wysyłki, połączenie z magazynem lub Allegro','od 2 500 zł','jednorazowo'),
 ('Kampanie reklamowe','Google, Facebook i Instagram, TikTok','od 700 zł','miesięcznie + budżet reklam')]
def ptable(rows=PRICES):
    return '<div class="tablewrap rv"><table class="ptable"><thead><tr><th>Usługa</th><th>Cena netto</th><th>Rozliczenie</th></tr></thead><tbody>'+''.join('<tr><td><b>%s</b><span>%s</span></td><td class="p">%s</td><td>%s</td></tr>'%r for r in rows)+'</tbody></table></div>'

FOOT='''<footer><div class="wrap">
<div class="ft-top"><div class="ft-brand"><a class="logo" href="index.html">ELOK<span>.</span></a><p>Automatyzacje, strony i marketing. Systemy szyte pod konkretną firmę.</p></div>
<div class="ft-cols"><div><h4>Usługi</h4><a href="automatyzacje.html">Automatyzacje</a><a href="strony.html">Strony i sklepy</a><a href="marketing.html">Marketing</a></div>
<div><h4>Firma</h4><a href="realizacje.html">Realizacje</a><a href="cennik.html">Cennik</a><a href="o-nas.html">O nas</a></div>
<div><h4>Kontakt</h4><span style="user-select:all">455 505 820</span><span style="user-select:all">kontakt@elok-agency.pl</span><a href="konsultacja.html" style="color:var(--gold)">Umów konsultację →</a></div></div></div>
<div class="ft-bot"><span>© 2026 ELOK · polska spółka</span><span><a href="#">Polityka prywatności</a> · <a href="#">Regulamin</a> · <a href="#">Cookies</a></span></div>
</div></footer><script src="site.js"></script>'''

def form(title='Porozmawiajmy <span class="g">o Twojej firmie.</span>',pre=None):
    return '''<section class="endcta"><div class="wrap"><div class="rv"><h2>%s</h2><p>Bezpłatna rozmowa online, około 30 minut. Wybierasz dzień i godzinę, a my się odzywamy.</p></div>
<div class="side rv"><a class="btn pri mag" href="konsultacja.html">Wybierz termin konsultacji <span class="ar">→</span></a><small>albo zadzwoń: <b>455 505 820</b> · pon–pt 9–17</small></div></div></section>'''%title

pages={}

# ---------- STRONA GŁÓWNA ----------
pages['index.html']=(head('ELOK Agency','Automatyzacje, strony i marketing dla firm. Systemy szyte pod konkretny biznes.',True),'''
<section class="hero"><canvas id="net" aria-hidden="true"></canvas><div class="wrap">
<div class="eyebrow">ELOK Agency</div>
<h1><span class="ln"><span>Technologia,</span></span><span class="ln"><span>która pracuje</span></span><span class="ln"><span><span class="rot" id="rot"><b class="on">za Ciebie.</b><b>całą dobę.</b><b>na Twój zysk.</b></span></span></span></h1>
<div class="bot"><p class="lead">Automatyzujemy pracę w firmach, budujemy strony i prowadzimy reklamy. Wszystko pod konkretną firmę i w jednym miejscu.</p>
<div class="btns"><a class="btn pri mag" href="#kontakt">Umów bezpłatną konsultację <span class="ar">→</span></a><a class="btn sec" href="realizacje.html">Zobacz realizacje</a></div></div></div></section>
<div class="mq" aria-label="Przykładowe narzędzia, z którymi łączymy systemy"><div class="lab">Łączymy narzędzia, których już używasz</div><div class="tr" id="mqt"><span>KSeF</span><span>WooCommerce</span><span>Allegro</span><span>Shopify</span><span>Google</span><span>Facebook</span><span>TikTok</span><span>Bramki SMS</span><span>Przelewy24</span><span>InPost</span><span>Excel</span><span>Gmail</span><span>Kalendarz</span><span>Hurtownie</span></div></div>

<section><div class="wrap">'''+shead('Czym się zajmujemy','Trzy usługi. <span class="g">Jeden zespół.</span>','Wybierz, co Cię interesuje. Na każdej stronie znajdziesz szczegóły, przykłady i ceny.')+'''
<div class="pillars">
<a class="pcard main rv tilt" href="automatyzacje.html"><div class="glow"></div><span class="n">GŁÓWNA SPECJALIZACJA</span><h3>Automatyzacje i systemy</h3><p>Rzeczy, które dziś robisz ręcznie, zaczynają dziać się same.</p><ul><li>panele i CRM pod Twoją firmę</li><li>faktury, KSeF i płatności</li><li>SMS-y, maile i przypomnienia</li><li>połączenie programów, których używasz</li></ul><div class="foot"><span class="price">od <b>600 zł</b> netto</span><span class="link">Zobacz →</span></div></a>
<a class="pcard rv tilt" href="strony.html"><div class="glow"></div><span class="n">USŁUGA</span><h3>Strony i sklepy</h3><p>Szybkie strony, z których zapytania trafiają prosto do Ciebie.</p><ul><li>strony firmowe</li><li>sklepy internetowe</li><li>widoczność w Google</li></ul><div class="foot"><span class="price">od <b>1 500 zł</b> netto</span><span class="link">Zobacz →</span></div></a>
<a class="pcard rv tilt" href="marketing.html"><div class="glow"></div><span class="n">DODATEK</span><h3>Marketing</h3><p>Reklamy, które przyprowadzają nowych klientów.</p><ul><li>Google</li><li>Facebook i Instagram</li><li>TikTok</li></ul><div class="foot"><span class="price">od <b>700 zł</b> netto / mc</span><span class="link">Zobacz →</span></div></a>
</div></div></section>

<section class="band"><div class="wrap">'''+shead('Realizacje','Systemy, które <span class="g">już działają.</span>','Prawdziwe zrzuty ekranu z wdrożonych systemów. Kliknij, żeby przeczytać więcej.')+CASES2+'''</div></section>

<section><div class="wrap">'''+shead('Jak wygląda współpraca','Cztery proste kroki.')+steps(STEPS)+'''</div></section>

<section class="band"><div class="wrap">'''+shead('Cennik','Ile to kosztuje?','Podajemy ceny „od”. Dokładną kwotę dostajesz po rozmowie, zanim cokolwiek zaczniemy.')+ptable()+'''<div style="margin-top:22px"><a class="link" href="cennik.html">Pełny cennik →</a></div></div></section>

<section><div class="wrap narrow">'''+shead('Pytania','Najczęstsze pytania')+faq(FAQ_MAIN)+'''</div></section>
'''+form('Porozmawiajmy <span class="g">o Twojej firmie.</span>'))

# ---------- AUTOMATYZACJE ----------
pages['automatyzacje.html']=(head('Automatyzacje i systemy · ELOK','Automatyzujemy pracę w firmach: panele, CRM, faktury, KSeF, SMS, integracje.'),
svc_hero('automatyzacje.html','Automatyzacje i systemy','Niech rutyna <span class="g">robi się sama.</span>','Budujemy panele i automaty dopasowane do Twojej firmy. Łączymy programy, których już używasz, i zdejmujemy z Ciebie ręczną robotę.','<div class="facts"><span>od <b>600 zł</b> netto</span><span>dla <b>każdej branży</b></span></div>',AUTO_VIS,'')+'''
<section class="band"><div class="wrap">'''+shead('Co możemy zautomatyzować','Najczęściej robimy <span class="g">te rzeczy.</span>','Masz inny pomysł? Też go zrobimy. To tylko przykłady.')+feats([
 ('calc','Wyceny i oferty','Oferta liczy się sama, a klient dostaje ją mailem lub SMS-em.',''),
 ('box','Zamówienia i magazyn','Zamówienia z kilku miejsc w jednym panelu, stany zawsze aktualne.',''),
 ('doc','Faktury i KSeF','Faktura z wyceny lub zamówienia, wysłana jednym kliknięciem.',''),
 ('bank','Płatności','System sam sprawdza wpłaty i przypomina o zaległych.',''),
 ('user','Klienci (CRM)','Historia klienta, dokumenty i statusy w jednym miejscu.',''),
 ('cal','Rezerwacje i SMS','Klient sam wybiera termin i dostaje przypomnienie.',''),
 ('chart','Raporty','Codzienne zestawienie czeka rano w Twojej skrzynce.',''),
 ('spark','Sztuczna inteligencja','Odpowiedzi na powtarzalne pytania i porządkowanie dokumentów.','')],'grid4')+'''</div></section>
<section><div class="wrap">'''+shead('Przykłady z branż','Zobacz, jak to działa <span class="g">w różnych firmach.</span>','Kliknij branżę, żeby zobaczyć przykład.')+AUTO_BLOCK%0+'''</div></section>
<section class="band"><div class="wrap">'''+shead('Realizacja','Działający system <span class="g">w serwisie samochodowym.</span>')+'''<div class="split">'''+shot('serwis.jpg','Baza ofert w systemie serwisu','Baza ofert w systemie serwisu')+'''<div class="rv"><div class="kpi" style="margin-bottom:20px"><b>−87%</b><span>czasu na przygotowanie wycen</span></div><p class="lead">Części z katalogu trafiają do wyceny jednym przyciskiem, ceny pobierają się z hurtowni, a faktura powstaje jednym kliknięciem.</p><div style="margin-top:26px"><a class="btn sec" href="realizacja-serwis.html">Przeczytaj całą realizację <span class="ar">→</span></a></div></div></div></div></section>
<section><div class="wrap narrow">'''+shead('Pytania','Pytania o automatyzacje')+faq([
 ('Czy automatyzacja zastąpi moich pracowników?','Nie. Zabiera im powtarzalne zadania, żeby mieli czas na klientów.'),
 ('Co, jeśli używam nietypowego programu?','Sprawdzimy, czy da się go podłączyć. Zwykle się da, a jeśli nie, szukamy innego rozwiązania.'),
 ('Czy to działa na telefonie?','Tak. Wszystkie panele działają na komputerze i w telefonie.'),
 ('Ile to kosztuje?','Automatyzacje zaczynają się od 600 zł netto. Dokładną cenę podajemy po rozmowie.'),
 ('Czy moje dane są bezpieczne?','Tak. Dostęp jest chroniony hasłem, a każda osoba widzi tylko to, co powinna.')])+'''</div></section>'''+form('Opowiedz, co zabiera Ci <span class="g">najwięcej czasu.</span>','o1'))

# ---------- STRONY ----------
pages['strony.html']=(head('Strony i sklepy · ELOK','Szybkie strony i sklepy internetowe, które zbierają zapytania i sprzedają.'),
svc_hero('strony.html','Strony i sklepy','Strona, która <span style="color:#7FD3C1">przynosi klientów.</span>','Projektujemy i budujemy szybkie strony i sklepy. Każde zapytanie z formularza od razu trafia do Twojego telefonu.','<div class="facts"><span>strona od <b>1 500 zł</b> netto</span><span>sklep od <b>2 500 zł</b> netto</span></div>',WEB_ANIM,'--tint:rgba(127,211,193,.14);--tc:#7FD3C1;--halo:rgba(127,211,193,.13)')+'''
<section class="band"><div class="wrap">'''+shead('Co dostajesz','W każdej stronie <span class="g">w standardzie.</span>')+feats([
 ('bolt','Szybkie ładowanie','Strona otwiera się błyskawicznie, także na telefonie.',''),
 ('phone','Wygodna na telefonie','Większość klientów wchodzi z telefonu, więc od tego zaczynamy.',''),
 ('in','Zapytania na telefon','Formularz od razu wysyła powiadomienie do Ciebie.',''),
 ('search','Widoczność w Google','Opisy, mapa strony i podstawy SEO od pierwszego dnia.',''),
 ('pen','Łatwa edycja','Teksty i zdjęcia zmieniasz sam w prostym panelu.',''),
 ('shield','Opieka po starcie','Pomagamy i poprawiamy, gdy coś trzeba zmienić.','')])+'''</div></section>
<section><div class="wrap">'''+shead('Rodzaje stron','Wybierz, czego potrzebujesz.')+'''<div class="grid3">
<div class="pc rv"><span class="lab">Landing page</span><div class="am"><small>od</small><b>1 500</b><em>zł netto</em></div><p>Jedna strona pod konkretną usługę albo reklamę.</p><ul><li>projekt i wykonanie</li><li>formularz z powiadomieniem</li><li>statystyki odwiedzin</li></ul></div>
<div class="pc rv hot"><span class="lab">Strona firmowa</span><div class="am"><small>od</small><b>1 500</b><em>zł netto</em></div><p>Kilka podstron: usługi, realizacje, cennik, kontakt.</p><ul><li>wszystko z landing page</li><li>podstrony i blog</li><li>panel do edycji</li></ul></div>
<div class="pc rv"><span class="lab">Sklep internetowy</span><div class="am"><small>od</small><b>2 500</b><em>zł netto</em></div><p>Sklep z płatnościami, wysyłką i magazynem.</p><ul><li>płatności i dostawy</li><li>połączenie z Allegro</li><li>szkolenie z obsługi</li></ul></div>
</div></div></section>
<section class="band"><div class="wrap">'''+shead('Jak powstaje strona','Od rozmowy <span class="g">do pierwszego zapytania.</span>')+steps([('Rozmowa','Ustalamy, dla kogo jest strona i co ma robić.'),('Projekt','Pokazujemy wygląd i poprawiamy, aż będzie dobrze.'),('Wykonanie','Budujemy stronę, teksty i formularze.'),('Start','Publikujemy i podpinamy zapytania pod Twój telefon.')])+'''</div></section>
<section><div class="wrap narrow">'''+shead('Pytania','Pytania o strony')+faq([
 ('Czy mogę sam zmieniać treści?','Tak, w prostym panelu, bez znajomości programowania.'),
 ('Mam już stronę. Musicie robić nową?','Nie zawsze. Najpierw sprawdzimy obecną i powiemy szczerze, co się bardziej opłaca.'),
 ('Pomożecie z tekstami?','Tak. Piszemy proste i konkretne teksty dla Twoich klientów.'),
 ('Czy strona będzie wysoko w Google?','Przygotowujemy ją pod Google, ale pozycja zależy też od konkurencji i czasu. Nie obiecujemy konkretnego miejsca.')])+'''</div></section>'''+form('Porozmawiajmy <span class="g">o Twojej stronie.</span>','o2'))

# ---------- MARKETING ----------
pages['marketing.html']=(head('Marketing · ELOK','Kampanie Google, Facebook i TikTok, które przyprowadzają klientów.'),
svc_hero('marketing.html','Marketing','Reklamy, które <span style="color:#F2A07B">przyprowadzają klientów.</span>','Prowadzimy kampanie w Google, na Facebooku, Instagramie i TikToku. Co miesiąc dostajesz prosty raport: ile wydaliśmy i ile było zapytań.','<div class="facts"><span>od <b>700 zł</b> netto / mc</span><span><b>raport</b> co miesiąc</span></div>',CHART,'--tint:rgba(242,160,123,.14);--tc:#F2A07B;--halo:rgba(242,160,123,.12)')+'''
<section class="band"><div class="wrap">'''+shead('Co robimy','Zajmujemy się <span class="g">całą kampanią.</span>')+feats([
 ('target','Plan i grupa klientów','Ustalamy, do kogo mówimy i z jaką ofertą.',''),
 ('pen','Reklamy','Piszemy teksty, robimy grafiki i krótkie filmy.',''),
 ('chart','Pomiar wyników','Widzisz, które reklamy dają zapytania.',''),
 ('search','Wizytówka Google','Porządkujemy wizytówkę, żeby klienci łatwo Cię znaleźli.',''),
 ('bolt','Poprawki co tydzień','Wyłączamy, co nie działa, wzmacniamy, co działa.',''),
 ('doc','Raport co miesiąc','Prosto i bez żargonu.','')])+'''</div></section>
<section><div class="wrap"><div class="callout rv"><div><b>Reklamy działają najlepiej z dobrą stroną</b><p>Kiedy klient kliknie, musi trafić na szybką stronę z prostym formularzem. Pomożemy też z tym.</p></div><a class="btn sec" href="strony.html">Zobacz strony <span class="ar">→</span></a></div></div></section>
<section class="band"><div class="wrap narrow">'''+shead('Pytania','Pytania o reklamy')+faq([
 ('Ile muszę wydać na reklamy?','Na początek wystarczy kilkadziesiąt złotych dziennie. Budżet płacisz bezpośrednio Google lub Facebookowi, osobno od naszej obsługi.'),
 ('Czy gwarantujecie wyniki?','Nie obiecujemy konkretnych liczb, bo zależą od rynku i konkurencji. Obiecujemy uczciwy raport i ciągłe poprawki.'),
 ('Czy muszę mieć nową stronę?','Nie zawsze. Przed startem sprawdzimy, czy Twoja strona nadaje się pod reklamy.')])+'''</div></section>'''+form('Sprawdźmy, gdzie są <span class="g">Twoi klienci.</span>','o3'))

# ---------- REALIZACJE ----------
pages['realizacje.html']=(head('Realizacje · ELOK','Systemy i automatyzacje wdrożone przez ELOK.'),
phero('Realizacje','Realizacje','Systemy, które <span class="g">pracują codziennie.</span>','Prawdziwe wdrożenia i prawdziwe zrzuty ekranu. Kliknij realizację, żeby przeczytać szczegóły.',btns=False)+'''
<section style="padding-top:0"><div class="wrap">'''+CASES2+'''<div class="callout rv" style="margin-top:30px"><div><b>Twoja firma może być następna</b><p>Opowiedz, jak pracujesz, a pokażemy, co da się usprawnić.</p></div><a class="btn pri mag" href="#kontakt">Umów konsultację <span class="ar">→</span></a></div></div></section>'''+form())

# ---------- CASE: SERWIS ----------
pages['realizacja-serwis.html']=(head('Case study: serwis samochodowy · ELOK','System dla serwisu samochodowego: katalog części, wycena, oferta online, faktura.'),
'''<section class="phero"><div class="wrap"><div class="crumbs"><a href="index.html">Strona główna</a> / <a href="realizacje.html">Realizacje</a> / Serwis samochodowy</div><span class="tagbig" style="display:inline-flex;gap:10px;font-weight:700;font-size:15px;padding:8px 16px;border-radius:999px;background:rgba(207,168,94,.14);color:var(--gold)">Realizacja · serwis samochodowy premium</span><h1 style="max-width:18ch">Od katalogu części do faktury <span class="g">bez przepisywania.</span></h1><p class="lead">System dla nieautoryzowanego serwisu premium. Części z katalogu trafiają prosto do wyceny, a wycena jednym kliknięciem staje się fakturą.</p>
<div class="kpis"><div class="rv"><b>−87%</b><span>czasu na przygotowanie wycen</span></div><div class="rv"><b>8 h 42 min</b><span>odzyskane każdego tygodnia</span></div><div class="rv"><b>0</b><span>ręcznie przepisywanych cen</span></div></div></div></section>
<section style="padding-top:0"><div class="wrap">'''+shead('Film','Zobacz, jak to działa <span class="g">na żywo.</span>','Nagranie ekranu z działającego systemu. Dane klientów są testowe.')+'''<div class="vplayer rv"><div class="top"><i></i><i></i><i></i><span>System serwisu · nagranie ekranu</span></div><video src="vid/serwis.mp4" poster="img/s-katalog.jpg" playsinline preload="metadata" muted></video><button class="ov" type="button" aria-label="Odtwórz film"><span><b>▶</b>Odtwórz film (25 s)</span></button></div><p class="vnote">Katalog części → wycena z rabatem → oferta dla klienta → faktura.</p></div></section>
<section class="band"><div class="wrap split"><div class="prose rv"><div class="eyebrow">Problem</div><h2 style="margin:16px 0 22px">Godziny na przepisywanie.</h2>
<p>Doradca szukał części w programie katalogowym i ręcznie przepisywał je do programu z ofertami. Ceny sprawdzał osobno u dostawcy, bo często się zmieniają.</p>
<p>Potem ręcznie robił PDF, wysyłał go mailem, a po naprawie wpisywał te same pozycje jeszcze raz do faktury. Zajmowało to nawet 10 godzin tygodniowo.</p></div>
<div class="ba rv" style="margin-top:0;grid-template-columns:1fr"><div class="bef"><h4>Przed</h4><ul><li>przepisywanie części z katalogu</li><li>sprawdzanie cen u dostawcy</li><li>PDF i mail robione ręcznie</li><li>te same pozycje drugi raz w fakturze</li></ul></div><div class="aft"><h4>Po</h4><ul><li>jeden przycisk w katalogu</li><li>aktualne ceny pobierają się same</li><li>oferta mailem lub jako link</li><li>faktura jednym kliknięciem</li></ul></div></div></div></section>
<section class="band"><div class="wrap">'''+shead('Ekrany','Krok po kroku.')+'''<div class="shots">'''+shot('s-katalog.jpg','1. W katalogu części klikasz „Wyślij do ELOK”','Katalog części z przyciskiem wysyłki do systemu')+shot('s-wycena.jpg','2. Ustawiasz rabat, ceny są już pobrane z hurtowni','Edycja wyceny z rabatami')+shot('s-oferta.jpg','3. Klient dostaje elegancką ofertę i PDF','Oferta dla klienta z logo')+shot('serwis.jpg','4. Wszystkie oferty w jednym miejscu, faktura jednym kliknięciem','Baza ofert')+'''</div></div></section>
<section class="band"><div class="wrap"><div class="shead rv"><div><div class="eyebrow">Efekt</div><h2>Z 10 godzin <span class="g">do 1 h 18 min tygodniowo.</span></h2></div><p class="lead">Klient szybciej dostaje wycenę i fakturę, a ceny w ofertach są zawsze aktualne.</p></div></div></section>'''+form('Chcesz podobny system <span class="g">u siebie?</span>'))

# ---------- CASE: PANEL ----------
pages['realizacja-panel.html']=(head('Case study: panel finansowy e-commerce · ELOK','Panel finansowo-zarządczy dla firmy e-commerce z dwiema markami.'),
'''<section class="phero"><div class="wrap"><div class="crumbs"><a href="index.html">Strona główna</a> / <a href="realizacje.html">Realizacje</a> / Panel finansowy</div><span style="display:inline-flex;font-weight:700;font-size:15px;padding:8px 16px;border-radius:999px;background:rgba(207,168,94,.14);color:var(--gold)">Realizacja · e-commerce</span><h1 style="max-width:18ch">Panel finansowy, <span class="g">który liczy sam.</span></h1><p class="lead">System dla firmy e-commerce, która prowadzi dwie marki. Raporty, oferty, analityka i podatki w jednym miejscu.</p>
<div class="kpis"><div class="rv"><b>2</b><span>marki rozliczane osobno, automatycznie</span></div><div class="rv"><b>1</b><span>panel zamiast kilku programów</span></div><div class="rv"><b>dziesiątki h</b><span>oszczędności każdego miesiąca</span></div></div></div></section>
<section style="padding-top:0"><div class="wrap">'''+shot('panel.jpg','Rozliczenie miesiąca: podatki osobno dla każdej marki i lista operacji','Panel finansowy z rozliczeniem')+'''</div></section>
<section class="band"><div class="wrap split"><div class="prose rv"><div class="eyebrow">Punkt wyjścia</div><h2 style="margin:16px 0 22px">Chaos w dokumentach.</h2><p>Raporty kasowe robione ręcznie, oferty w osobnych programach, a do tego podatki liczone osobno dla dwóch marek. Co miesiąc to samo zamieszanie.</p></div>
<div class="ba rv" style="margin-top:0;grid-template-columns:1fr"><div class="bef"><h4>Przed</h4><ul><li>ręczne raporty kasowe</li><li>oferty w osobnych programach</li><li>ręczny podział podatków</li></ul></div><div class="aft"><h4>Po</h4><ul><li>raport kasowy z eksportem do PDF i CSV</li><li>osobne rozliczenie każdej marki</li><li>zysk netto widoczny na bieżąco</li></ul></div></div></div></section>
<section><div class="wrap">'''+shead('Moduły','Cztery części <span class="g">jednego panelu.</span>')+feats([
 ('doc','Raport kasowy','Dowody KP i KW w jednym miejscu, eksport jednym kliknięciem.',''),
 ('layers','Podział na marki','Każda transakcja trafia do właściwej marki, podatki liczą się osobno.',''),
 ('calc','Oferty','Kosztorysy w kilka sekund i archiwum gotowe do PDF.',''),
 ('chart','Analityka','Zysk netto na bieżąco, zamknięte miesiące w archiwum.','')],'grid4')+'''</div></section>'''+form('Chcesz mieć finanse <span class="g">w jednym panelu?</span>'))

# ---------- CENNIK ----------
pages['cennik.html']=(head('Cennik · ELOK','Cennik ELOK: automatyzacje od 600 zł, strony od 1 500 zł, sklepy od 2 500 zł, reklamy od 700 zł/mc.'),
phero('Cennik','Cennik','Ile to <span class="g">kosztuje?</span>','Poniżej ceny startowe. Dokładną cenę podajemy po krótkiej, bezpłatnej rozmowie, zawsze przed rozpoczęciem pracy.',btns=False)+'''
<section style="padding-top:0"><div class="wrap">'''+ptable()+'''<p class="disc" style="font-size:16px">Wszystkie ceny są netto (bez VAT). Budżet na reklamy płacisz bezpośrednio Google lub Facebookowi.</p>
<div class="callout rv"><div><b>Nie wiesz, czego potrzebujesz?</b><p>Nic nie szkodzi. Opowiedz nam o firmie, a doradzimy i podamy cenę.</p></div><a class="btn pri mag" href="#kontakt">Zapytaj o cenę <span class="ar">→</span></a></div></div></section>
<section class="band"><div class="wrap">'''+shead('Od czego zależy cena','Trzy rzeczy, które <span class="g">mają znaczenie.</span>')+feats([
 ('layers','Wielkość projektu','Ile funkcji, podstron albo procesów chcesz mieć.',''),
 ('link','Połączenia','Z iloma programami, hurtowniami lub bankami trzeba się połączyć.',''),
 ('pen','Treści','Czy masz teksty i zdjęcia, czy przygotowujemy je od zera.','')])+'''</div></section>
<section><div class="wrap narrow">'''+shead('Pytania','Pytania o płatności')+faq([
 ('Czy cena może się zmienić w trakcie?','Nie, jeśli zakres się nie zmienia. Jeśli zechcesz coś dodać, najpierw dostaniesz wycenę.'),
 ('Jak wygląda płatność?','Zwykle część na start i resztę po odbiorze. Szczegóły ustalamy w umowie.'),
 ('Czy wystawiacie fakturę VAT?','Tak. ELOK to polska spółka.'),
 ('Czy rozmowa jest płatna?','Nie. Pierwsza konsultacja jest bezpłatna i do niczego nie zobowiązuje.')])+'''</div></section>'''+form('Zapytaj o cenę <span class="g">dla swojej firmy.</span>','o4'))

# ---------- O NAS ----------
pages['o-nas.html']=(head('O nas · ELOK','ELOK łączy automatyzacje, strony i marketing w jeden system.'),
phero('O nas','O nas','Sami prowadzimy firmy. <span class="g">Wiemy, co działa.</span>','ELOK powstało, bo sami szukaliśmy partnera, który zrozumie biznes, a nie tylko wykona zadanie. Nie znaleźliśmy, więc zrobiliśmy to sami.',btns=False)+'''
<section class="band"><div class="wrap split"><div class="prose rv"><div class="eyebrow">Skąd się wzięliśmy</div><h2 style="margin:16px 0 22px">Z praktyki, nie z teorii.</h2>
<p>Wywodzimy się z e-commerce i usług. Systemy, które dziś budujemy dla klientów, najpierw sprawdzaliśmy we własnych projektach.</p>
<p>Robimy trzy rzeczy, które zwykle robią trzy różne firmy: automatyzacje, strony i marketing. Dzięki temu masz jeden kontakt i wszystko działa razem.</p></div>
<div class="rv"><ul class="list"><li><i>01</i><div><b>Najpierw rozmowa</b><span>Poznajemy, jak pracujesz, zanim cokolwiek zaproponujemy.</span></div></li><li><i>02</i><div><b>Mówimy wprost</b><span>Jeśli coś się nie opłaca, powiemy to otwarcie.</span></div></li><li><i>03</i><div><b>Solidna robota</b><span>Szybkie strony i systemy, które da się rozwijać.</span></div></li><li><i>04</i><div><b>Zostajemy na dłużej</b><span>Po starcie pomagamy i rozwijamy.</span></div></li></ul></div></div></section>'''+form('Poznajmy się <span class="g">na 30 minut.</span>'))

# ---------- KONSULTACJA ----------
pages['konsultacja.html']=(head('Umów konsultację · ELOK','Wybierz dzień i godzinę bezpłatnej konsultacji z ELOK.'),
'''<section class="phero" style="padding-bottom:30px"><div class="wrap"><div class="crumbs"><a href="index.html">Strona główna</a> / Konsultacja</div><h1>Umów bezpłatną <span class="g">konsultację.</span></h1><p class="lead">Wybierz dzień i godzinę. Rozmawiamy online około 30 minut. Bez zobowiązań.</p></div></section>
<section style="padding-top:20px"><div class="wrap book">
<div><div class="bblock"><div class="bstep" id="st1"><i>1</i><b>Wybierz dzień</b></div><div class="days" id="days" role="group" aria-label="Dni"></div></div>
<div class="bblock"><div class="bstep" id="st2"><i>2</i><b>Wybierz godzinę</b></div><div class="slots" id="slots" role="group" aria-label="Godziny"></div></div></div>
<div class="bside"><div class="bstep"><i>3</i><b>Twoje dane</b></div>
<form class="bform" id="bform" novalidate><div class="bsum" id="bsum">Najpierw wybierz dzień i godzinę.</div>
<label for="b-imie">Imię i nazwisko<input id="b-imie" autocomplete="name" placeholder="np. Marek Kowalski" required></label>
<label for="b-tel">Telefon<input id="b-tel" type="tel" autocomplete="tel" placeholder="np. 600 123 456" required></label>
<label for="b-mail">E-mail<input id="b-mail" type="email" autocomplete="email" placeholder="np. marek@firma.pl"></label>
<label for="b-opis">O czym chcesz porozmawiać? (opcjonalnie)<textarea id="b-opis" rows="2" placeholder="np. chcę zautomatyzować faktury"></textarea></label>
<button class="btn pri mag" type="submit" style="justify-content:center;margin-top:6px">Zarezerwuj termin <span class="ar">→</span></button>
<p class="note" style="font-size:14px">Potwierdzenie wyślemy SMS-em i mailem. Wysyłając, zgadzasz się na kontakt w sprawie konsultacji.</p></form>
<div class="bdone" id="bdone"><h3>Dziękujemy, termin zarezerwowany.</h3><p>Do zobaczenia: <b class="g" id="bdt"></b>. Potwierdzenie z linkiem do rozmowy dostaniesz SMS-em i mailem.</p></div>
<div class="lst" style="display:grid;gap:12px;margin-top:34px"><div style="display:flex;gap:12px"><span class="g">✓</span>30 minut online, bez zobowiązań</div><div style="display:flex;gap:12px"><span class="g">✓</span>Konkretne pomysły dla Twojej firmy</div><div style="display:flex;gap:12px"><span class="g">✓</span><span>Wolisz telefon? Zadzwoń: <b style="user-select:all;white-space:nowrap">455 505 820</b></span></div></div>
</div></div></section>''')

# ---------- KONTAKT ----------
pages['kontakt.html']=(head('Kontakt · ELOK','Kontakt z ELOK: telefon 455 505 820, kontakt@elok-agency.pl.'),
'''<section class="phero"><div class="wrap"><div class="crumbs"><a href="index.html">Strona główna</a> / Kontakt</div><h1>Porozmawiajmy <span class="g">o Twojej firmie.</span></h1><p class="lead">Najprościej: wybierz termin bezpłatnej konsultacji. Możesz też zadzwonić albo napisać.</p>
<div class="btns" style="margin-top:30px"><a class="btn pri mag" href="konsultacja.html">Wybierz termin konsultacji <span class="ar">→</span></a></div>
<div class="contactrow"><div><small>Telefon</small><b>455 505 820</b></div><div><small>E-mail</small><b>kontakt@elok-agency.pl</b></div><div><small>Godziny</small><b>pon–pt, 9–17</b></div></div></div></section>''')

