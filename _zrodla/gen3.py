#!/usr/bin/env python3
# Uruchamiać z katalogu v3: python3 gen3.py
exec(open('gen2_body.py').read())

FOOT = '''<footer class="pf"><div class="wrap">
<div class="lead-row"><h3>Masz w firmie coś, co <span class="g">zjada czas?</span> Pokażemy, jak oddać to systemowi.</h3>
<div class="act"><a class="btn pri mag" href="konsultacja.html">Umów bezpłatną konsultację <span class="ar">→</span></a><span style="color:var(--mut);font-size:15.5px">30 minut online · bez zobowiązań</span></div></div>
<div class="fstage"><div class="mark" aria-hidden="true">ELOK<span>.</span></div><div class="cols">
<div><h4>Usługi</h4><a href="automatyzacje.html">Automatyzacje i systemy</a><a href="strony.html">Strony i sklepy</a><a href="marketing.html">Marketing</a><a href="cennik.html">Cennik</a></div>
<div><h4>Firma</h4><a href="realizacje.html">Realizacje</a><a href="o-nas.html">O nas</a><a href="kontakt.html">Kontakt</a><a href="konsultacja.html">Konsultacja</a></div>
<div><h4>Kontakt</h4><span style="user-select:all">455 505 820</span><span style="user-select:all">kontakt@elok-agency.pl</span><span class="m">odpowiadamy w 1 dzień roboczy</span></div>
<div><h4>Godziny</h4><span>poniedziałek – piątek</span><span>9:00 – 17:00</span><span class="m">konsultacje online w całej Polsce</span></div>
</div></div>
<div class="legal"><span>© 2026 ELOK · polska spółka · faktura VAT</span><span><a href="#">Polityka prywatności</a> · <a href="#">Regulamin</a> · <a href="#">Cookies</a></span></div>
</div></footer><script src="site.js"></script>'''

def form(title='Porozmawiajmy <span class="g">o Twojej firmie.</span>', pre=None):
    return ('<section class="endcta"><div class="wrap"><div class="rv"><h2>%s</h2><p>Bezpłatna rozmowa online, około 30 minut. '
            'Wybierasz dzień i godzinę w kalendarzu, a potwierdzenie przychodzi na maila.</p></div>'
            '<div class="side rv"><a class="btn pri mag" href="konsultacja.html">Wybierz termin konsultacji <span class="ar">→</span></a>'
            '<small>albo zadzwoń: <b>455 505 820</b> · pon–pt 9–17</small></div></div></section>') % title

# ---------- KONSULTACJA ----------
KONS = '''<section class="phero" style="padding-bottom:30px"><div class="wrap"><div class="crumbs"><a href="index.html">Strona główna</a> / Konsultacja</div><h1>Umów bezpłatną <span class="g">konsultację.</span></h1><p class="lead">Wybierz dzień w kalendarzu i wolną godzinę. Rozmawiamy online około 30 minut. Bez zobowiązań.</p></div></section>
<section style="padding-top:20px"><div class="wrap book">
<div><div class="bblock"><div class="bstep" id="st1"><i>1</i><b>Wybierz dzień</b></div>
<div class="cal" id="cal"><div class="ch"><button type="button" id="cprev" aria-label="Poprzedni miesiąc">←</button><b id="clab"></b><button type="button" id="cnext" aria-label="Następny miesiąc">→</button></div>
<div class="wd"><span>pon</span><span>wt</span><span>śr</span><span>czw</span><span>pt</span><span>sob</span><span>nd</span></div><div class="grid" id="cgrid"></div>
<div class="leg"><span>dostępny dzień</span><span class="g2">wybrany</span></div></div></div>
<div class="bblock"><div class="bstep" id="st2"><i>2</i><b>Wybierz godzinę</b></div><p class="slotdate" id="slotdate"></p><div class="slots" id="slots" role="group" aria-label="Godziny"></div></div></div>
<div class="bside"><div class="bstep"><i>3</i><b>Twoje dane</b></div>
<form class="bform" id="bform" novalidate><div class="bsum" id="bsum"></div>
<label for="b-imie">Imię i nazwisko<input id="b-imie" autocomplete="name" placeholder="np. Marek Kowalski" required></label>
<label for="b-mail">E-mail<input id="b-mail" type="email" autocomplete="email" placeholder="np. marek@firma.pl" required></label>
<label for="b-tel">Telefon (opcjonalnie)<input id="b-tel" type="tel" autocomplete="tel" placeholder="np. 600 123 456"></label>
<label for="b-opis">O czym chcesz porozmawiać? (opcjonalnie)<textarea id="b-opis" rows="2" placeholder="np. chcę zautomatyzować faktury"></textarea></label>
<button class="btn pri mag" type="submit" style="justify-content:center;margin-top:6px">Zarezerwuj termin <span class="ar">→</span></button>
<p class="note" style="font-size:14px">Potwierdzenie z linkiem do rozmowy wyślemy na Twój e-mail. Wysyłając, zgadzasz się na kontakt w sprawie konsultacji.</p></form>
<div class="bdone" id="bdone"><h3>Dziękujemy, termin zarezerwowany.</h3><p>Do zobaczenia: <b class="g" id="bdt"></b>. Potwierdzenie z linkiem do rozmowy wyślemy na Twój e-mail.</p></div>
<div style="display:grid;gap:12px;margin-top:34px;font-size:17px"><div style="display:flex;gap:12px"><span class="g">✓</span>30 minut online, bez zobowiązań</div><div style="display:flex;gap:12px"><span class="g">✓</span>Konkretne pomysły dla Twojej firmy</div><div style="display:flex;gap:12px"><span class="g">✓</span><span>Wolisz telefon? Zadzwoń: <b style="user-select:all;white-space:nowrap">455 505 820</b></span></div></div>
</div></div></section>'''
pages['konsultacja.html'] = (head('Umów konsultację · ELOK', 'Wybierz dzień i godzinę bezpłatnej konsultacji z ELOK.'), KONS)

# ---------- KONTAKT ----------
KONT = ('''<section class="phero"><div class="wrap"><div class="crumbs"><a href="index.html">Strona główna</a> / Kontakt</div><h1>Porozmawiajmy <span class="g">o Twojej firmie.</span></h1><p class="lead">Wybierz sposób, który Ci pasuje. Na każdą wiadomość odpowiadamy w ciągu jednego dnia roboczego.</p></div></section>
<section style="padding-top:0"><div class="wrap"><div class="cards3">
<div class="ccard hl rv">''' + ico('cal') + '''<small>Najszybciej</small><div class="big">Konsultacja online</div><p>Wybierz dzień i godzinę w kalendarzu. 30 minut, bezpłatnie i bez zobowiązań.</p><a class="btn pri mag" href="konsultacja.html">Wybierz termin <span class="ar">→</span></a></div>
<div class="ccard rv">''' + ico('phone') + '''<small>Telefon</small><div class="big">455 505 820</div><p>Poniedziałek – piątek, 9:00 – 17:00. Jeśli nie odbierzemy, oddzwonimy.</p><button class="btn sec" type="button" data-copy="455505820">Kopiuj numer</button></div>
<div class="ccard rv">''' + ico('in') + '''<small>E-mail</small><div class="big">kontakt@elok-agency.pl</div><p>Opisz krótko, czym zajmuje się firma i co chcesz usprawnić.</p><button class="btn sec" type="button" data-copy="kontakt@elok-agency.pl">Kopiuj adres</button></div>
</div></div></section>
<section class="band"><div class="wrap split"><div class="rv"><div class="eyebrow">Co dalej</div><h2 style="margin:12px 0 18px">Tak wygląda <span class="g">pierwszy kontakt.</span></h2><p class="lead">Bez presji i bez sprzedawania na siłę. Najpierw chcemy zrozumieć, jak pracujesz.</p></div>
<div class="tline rv" style="margin-top:0"><div><b>Rozmowa, 30 minut</b><p>Opowiadasz o firmie i o tym, co zabiera Ci najwięcej czasu.</p></div><div><b>Nasze pomysły</b><p>Mówimy, co da się usprawnić, ile to może kosztować i od czego warto zacząć.</p></div><div><b>Plan i wycena na maila</b><p>W ciągu kilku dni dostajesz konkretny plan z ceną. Decyzja należy do Ciebie.</p></div></div></div></section>
<section><div class="wrap narrow">''' + shead('Pytania', 'Zanim napiszesz') + faq([
    ('Czy konsultacja jest płatna?', 'Nie. Pierwsza rozmowa jest bezpłatna i do niczego nie zobowiązuje.'),
    ('Czy muszę się przygotować?', 'Nie musisz. Wystarczy, że opowiesz, jak wygląda dzień w Twojej firmie.'),
    ('Gdzie się spotykamy?', 'Online. Link do rozmowy wideo dostaniesz mailem. Pracujemy z firmami z całej Polski.'),
    ('Jak szybko odpowiadacie?', 'Na maile i wiadomości odpowiadamy w ciągu jednego dnia roboczego.')]) + '</div></section>')
pages['kontakt.html'] = (head('Kontakt · ELOK', 'Kontakt z ELOK: telefon 455 505 820, kontakt@elok-agency.pl, konsultacje online.'), KONT)

# ---------- O NAS ----------
ONAS = (phero('O nas', 'O nas', 'Sami prowadzimy firmy. <span class="g">Dlatego wiemy, co działa.</span>',
              'ELOK to zespół praktyków. Zanim zaczęliśmy budować systemy dla innych, budowaliśmy je dla własnych firm i sprawdzaliśmy na własnych pieniądzach.', btns=False)
 + '''<section class="band"><div class="wrap split"><div class="prose rv"><div class="eyebrow">Skąd się wzięliśmy</div><h2 style="margin:12px 0 22px">Byliśmy po drugiej stronie.</h2>
<p>Technologia i marketing interesowały nas od zawsze. Kiedy jednak prowadziliśmy własne projekty, zabrakło nam czasu na stronę techniczną i zaczęliśmy szukać agencji.</p>
<p>Wtedy poznaliśmy problem od strony klienta: te same gotowe rozwiązania dla wszystkich, mało zrozumienia dla biznesu i dużo słów, których nikt nie tłumaczył.</p>
<p>Postanowiliśmy zrobić to inaczej. Tak powstało ELOK, firma, która najpierw słucha, potem doradza, a dopiero na końcu buduje.</p></div>
<div class="rv"><p class="quote">Budujemy to, czego sami szukaliśmy jako przedsiębiorcy.</p></div></div></section>
<section><div class="wrap">''' + shead('Co nas wyróżnia', 'Cztery rzeczy, <span class="g">na które możesz liczyć.</span>') + feats([
    ('target', 'Najpierw biznes', 'Zaczynamy od rozmowy o tym, jak pracujesz. Technologię dobieramy dopiero potem.', ''),
    ('layers', 'Wszystko w jednym miejscu', 'Automatyzacje, strona i reklamy od jednego zespołu. Masz jeden kontakt.', ''),
    ('shield', 'Sprawdzone u nas', 'Rozwiązania, które proponujemy, najpierw testujemy we własnych projektach.', ''),
    ('user', 'Mówimy po ludzku', 'Bez żargonu. Tłumaczymy prosto, co robimy, ile to kosztuje i co z tego masz.', '')], 'grid4')
 + '''</div></section>
<section class="band"><div class="wrap">''' + shead('Jak pracujemy', 'Zasady, których <span class="g">się trzymamy.</span>') + '''<div class="bignum">
<div class="rv"><b>Cena przed startem</b><span>Zawsze wiesz, ile zapłacisz, zanim zaczniemy. Bez niespodzianek na fakturze.</span></div>
<div class="rv"><b>Szczerość</b><span>Jeśli coś się nie opłaca, powiemy to wprost. Także wtedy, gdy oznacza to mniejsze zlecenie.</span></div>
<div class="rv"><b>Opieka po wdrożeniu</b><span>Nie znikamy po starcie. Pomagamy, poprawiamy i rozwijamy system razem z Twoją firmą.</span></div>
</div></div></section>
<section><div class="wrap split"><div class="rv"><div class="eyebrow">Branże</div><h2 style="margin:12px 0 18px">Znamy je <span class="g">od środka.</span></h2><p class="lead">Najlepiej znamy branże, w których sami działamy na co dzień.</p>
<div class="tags"><span>Motoryzacja i serwisy</span><span>E-commerce i sklepy</span><span>Usługi lokalne</span><span>Biura i gabinety</span><span>Handel</span></div></div>
<div class="prose rv"><div class="eyebrow">Poza pracą</div><h3 style="margin:12px 0 14px">Lubimy precyzję.</h3><p>Po pracy sport, motoryzacja i technologia. Fascynuje nas to, jak tysiące elementów składają się w jeden, dobrze działający silnik.</p><p>Tak samo patrzymy na firmy naszych klientów. Każdy proces ma działać płynnie, bez zgrzytów i bez zbędnej pracy.</p></div></div></section>
<section class="band"><div class="wrap">''' + shead('Realizacje', 'Zobacz, <span class="g">co już zbudowaliśmy.</span>') + CASES2 + '</div></section>'
 + form('Poznajmy się <span class="g">na 30 minut.</span>'))
pages['o-nas.html'] = (head('O nas · ELOK', 'Poznaj ELOK: zespół, który łączy automatyzacje, strony i marketing w jeden system.'), ONAS)

# pozostałe strony mają zakończenie z form() wyliczone wcześniej; podmieniamy stare zakończenie na nowe
import re
for k in list(pages):
    h, body = pages[k]
    body = re.sub(r'albo zadzwoń: <b>455 505 820</b> · pon–pt 9–17</small>', 'albo zadzwoń: <b>455 505 820</b> · pon–pt 9–17</small>', body)
    body = body.replace('Wybierasz dzień i godzinę, a my się odzywamy.', 'Wybierasz dzień i godzinę w kalendarzu, a potwierdzenie przychodzi na maila.')
    body = re.sub(r'<section class="endcta">.*?</section>', '', body, flags=re.S)
    pages[k] = (h, body)

exec(open('gen_loop.py').read())
