# Generuje landing pages pod kampanie Google Ads: strona-dla-firmy, sklep-internetowy, automatyzacja-ai.
# UWAGA: po wdrożeniu teksty landingów edytuje się w panelu (Edytor strony). Nie uruchamiaj ponownie bez przeniesienia tamtych zmian, bo je nadpiszesz.
# Uruchom: python3 _zrodla/landingi.py  (z katalogu repo)
import os, html

V = '2611121300'
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TICK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7"/></svg>'
IC = {
 'phone': '<path d="M7 2h10v20H7z"/><path d="M11 18h2"/>',
 'clock': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 'search': '<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/>',
 'cart': '<path d="M5 8h14l-1.5 12h-11z"/><path d="M9 8a3 3 0 016 0"/>',
 'box': '<path d="M3 7h11v9H3zM14 10h4l3 3v3h-7"/><circle cx="7" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>',
 'sync': '<path d="M20 12a8 8 0 01-14 5M4 12a8 8 0 0114-5"/><path d="M18 3v4h-4M6 21v-4h4"/>',
 'mail': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
 'doc': '<path d="M6 3h9l4 4v14H6z"/><path d="M9 12h6M9 16h4"/>',
 'bolt': '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
 'chat': '<path d="M4 5h16v11H8l-4 4z"/><path d="M8 9h8M8 12h5"/>',
 'eye': '<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
}
def ic(k): return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">' + IC[k] + '</svg>'
def e(s): return html.escape(s, quote=True)

PAGES = [
 dict(
  slug='strona-dla-firmy', zrodlo='strona',
  title='Strona internetowa dla firmy od 800 zł · ELOK',
  desc='Nowoczesna strona internetowa dla firmy od 800 zł netto. Zapytania z formularza od razu trafiają na Twój telefon. Bezpłatna wycena w 24 godziny.',
  eye='Strony internetowe dla firm',
  h1='Strona, która <span class="g">sama zbiera klientów.</span>',
  lead='Projektujemy szybkie, nowoczesne strony dla firm. Każde zapytanie z formularza od razu trafia na Twój telefon, a klient dostaje automatyczną odpowiedź.',
  price=('od 800 zł', 'netto, jednorazowo · cenę znasz przed startem'),
  ticks=['Wygląda dobrze na telefonie, a stamtąd wchodzi większość klientów', 'Zapytania prosto na telefon, bez sprawdzania skrzynki', 'Podstawy SEO i statystyki: widzisz, skąd przychodzą klienci'],
  co=['Nowa strona firmowa', 'Odświeżenie starej strony', 'Landing pod reklamy', 'Jeszcze nie wiem'],
  ph='np. warsztat w Piasecznie, chcę stronę z cennikiem i formularzem',
  probs=[('eye','Strona nie przynosi zapytań','Ładna wizytówka, ale telefon milczy. Projektujemy stronę tak, żeby prowadziła klienta prosto do kontaktu.'),
         ('phone','Na telefonie wszystko się rozjeżdża','Większość ludzi wchodzi z telefonu. Każdą stronę robimy najpierw pod telefon, potem pod komputer.'),
         ('clock','Zapytania giną albo czekają','Formularz wysyła powiadomienie na telefon od razu. Odpowiadasz, zanim klient zadzwoni do konkurencji.')],
  inc=['Projekt graficzny pod Twoją firmę','Wersja na telefon i komputer','Formularz z powiadomieniem na telefon','Podstawy SEO','Statystyki odwiedzin','Teksty i zdjęcia ułożone za Ciebie','Polityka prywatności i cookies','Poprawki po starcie'],
  case=('Ta strona też jest nasza', 'Strona ELOK, na której jesteś, to nasza robota: zapytania i rezerwacje lądują w panelu i na telefonie, a teksty edytujemy sami bez programisty.', [('Formularz na stronie','klient'),('Powiadomienie na telefon','od razu'),('Odpowiedź do klienta','automatycznie')], 'index.html', 'Zobacz całą stronę ELOK'),
  faq=[('Ile kosztuje strona internetowa?','Prosta strona firmowa albo landing zaczyna się od 800 zł netto. Większe strony z wieloma podstronami wyceniamy po krótkiej rozmowie. Cenę znasz przed startem i się nie zmienia.'),
       ('Ile trwa zrobienie strony?','Zależy od wielkości strony i tego, jak szybko mamy od Ciebie teksty i zdjęcia. Termin ustalamy przed startem.'),
       ('Czy muszę mieć gotowe teksty i zdjęcia?','Nie. Ułożymy teksty za Ciebie na podstawie rozmowy, a zdjęcia dobierzemy albo podpowiemy, co sfotografować.'),
       ('Czy później sam mogę zmieniać teksty?','Tak. Pokażemy, jak to zrobić, albo zmienimy za Ciebie.'),
       ('Czy wystawiacie fakturę VAT?','Tak, jesteśmy polską spółką i wszystko jest na fakturę.')],
  final='Sprawdź, ile będzie kosztować Twoja strona.'),
 dict(
  slug='sklep-internetowy', zrodlo='sklep',
  title='Sklep internetowy od 1 800 zł · ELOK',
  desc='Sklep internetowy z płatnościami i wysyłkami od 1 800 zł netto. Połączenie z magazynem lub Allegro jako dodatek. Bezpłatna wycena w 24 godziny.',
  eye='Sklepy internetowe',
  h1='Sklep, który <span class="g">sprzedaje, a nie tylko wisi.</span>',
  lead='Robimy sklepy z płatnościami, wysyłkami i połączeniem z magazynem lub Allegro. Zamówienia, stany i dokumenty dzieją się same, a Ty zajmujesz się sprzedażą.',
  price=('od 1 800 zł', 'netto, jednorazowo · cenę znasz przed startem'),
  ticks=['Płatności online i wysyłki gotowe od pierwszego dnia', 'Stany i ceny z magazynu lub hurtowni aktualizują się same', 'Szkolenie z obsługi, żebyś nie był od nas zależny'],
  co=['Nowy sklep', 'Przeniesienie obecnego sklepu', 'Połączenie z Allegro lub hurtownią', 'Jeszcze nie wiem'],
  ph='np. sprzedaję części na Allegro, chcę własny sklep z tymi samymi stanami',
  probs=[('sync','Ręczne przepisywanie stanów i cen','Sklep łączymy z magazynem, hurtownią lub Allegro. Stany i ceny zmieniają się same, bez arkuszy.'),
         ('box','Każde zamówienie to kilka programów','Płatność, etykieta, mail do klienta i dokumenty dzieją się po kolei same, w jednym miejscu.'),
         ('cart','Klienci odchodzą przy koszyku','Prosty koszyk, szybkie płatności i sklep dobrze działający na telefonie. Mniej porzuconych zamówień.')],
  inc=['Projekt pod Twoją markę','Karty produktów i koszyk','Płatności online','Wysyłki i kurierzy','Połączenie z magazynem lub Allegro','Wersja na telefon','Podstawy SEO','Szkolenie z obsługi'],
  case=('Sklep z częściami samochodowymi', 'Sklep z oryginalnymi częściami: ceny i stany pobierane z hurtowni, a zamówienia, wysyłki i dokumenty obsługują się automatycznie.', [('Hurtownia','ceny i stany'),('Sklep','aktualny co noc'),('Zamówienie','faktura i etykieta same')], 'realizacja-sklep.html', 'Zobacz case study'),
  faq=[('Ile kosztuje sklep internetowy?','Sklep zaczyna się od 1 800 zł netto. Cena zależy głównie od liczby produktów i połączeń (magazyn, hurtownia, Allegro). Cenę znasz przed startem.'),
       ('Na jakiej platformie robicie sklepy?','Dobieramy platformę do Twojej sprzedaży: najczęściej WooCommerce albo rozwiązanie szyte na miarę. Podpowiemy na rozmowie, co ma sens u Ciebie.'),
       ('Czy można połączyć sklep z Allegro?','Tak. Stany, ceny i zamówienia mogą być wspólne dla sklepu i Allegro.'),
       ('Czy przeniesiecie mój obecny sklep?','Tak, przenosimy produkty, klientów i zamówienia z obecnej platformy.'),
       ('Czy wystawiacie fakturę VAT?','Tak, jesteśmy polską spółką i wszystko jest na fakturę.')],
  final='Sprawdź, ile będzie kosztować Twój sklep.'),
 dict(
  slug='automatyzacja-ai', zrodlo='automatyzacja',
  title='Automatyzacja i AI w firmie · ELOK',
  desc='Wdrażamy automatyzacje i AI w małych firmach: faktury, maile, oferty, zamówienia i raporty, które robią się same. Automatyzacje od 600 zł netto. Bezpłatna konsultacja.',
  eye='Automatyzacja i AI dla firm',
  h1='Powtarzalna praca <span class="g">może robić się sama.</span>',
  lead='Faktury, maile, oferty, zamówienia i raporty mogą robić się same. Sprawdzamy, co w Twojej firmie zjada najwięcej czasu, i wdrażamy automatyzacje na Twoich danych.',
  price=('od 600 zł', 'netto za automatyzację · większe systemy po rozmowie'),
  ticks=['Zaczynamy od tego, co zjada najwięcej czasu', 'Działa z programami, których już używasz', 'Testy na Twoich danych i instrukcja dla zespołu'],
  co=['Faktury i dokumenty', 'Maile i obsługa klienta', 'Oferty i wyceny', 'Zamówienia i magazyn', 'Raporty', 'Jeszcze nie wiem'],
  ph='np. codziennie ręcznie przepisuję zamówienia do faktur',
  probs=[('doc','Ręczne przepisywanie danych','Zamówienie, faktura, KSeF, mail do klienta. Łączymy programy tak, żeby dane szły same.'),
         ('chat','Te same maile i pytania codziennie','AI przygotowuje odpowiedzi, oferty i opisy na podstawie Twoich danych. Ty tylko sprawdzasz i klikasz.'),
         ('bolt','Nie wiesz, co się dzieje w firmie','Raport na maila co rano: sprzedaż, zamówienia, co czeka. Bez otwierania pięciu programów.')],
  inc=['Analiza Twojego procesu','Plan: co automatyzujemy najpierw','Wdrożenie i testy na Twoich danych','Połączenie z obecnymi programami','AI tam, gdzie naprawdę pomaga','Instrukcja dla zespołu','Poprawki po starcie','Możliwość rozbudowy krok po kroku'],
  case=('System dla serwisu samochodowego', 'Katalog części, wycena, oferta online i faktura w jednym systemie. To, co wcześniej zajmowało kilka programów i telefonów, dzieje się w kilka kliknięć.', [('Katalog części','cena od razu'),('Oferta online','klient akceptuje'),('Faktura','KSeF automatycznie')], 'realizacja-serwis.html', 'Zobacz case study'),
  faq=[('Ile kosztuje automatyzacja?','Pojedyncza automatyzacja, np. faktura po zamówieniu albo raport na maila, zaczyna się od 600 zł netto. Większe systemy i panele wyceniamy po rozmowie. Cenę znasz przed startem.'),
       ('Czy muszę zmieniać programy, których używam?','Zwykle nie. Najczęściej łączymy to, co już masz: sklep, program do faktur, pocztę, arkusze.'),
       ('Do czego realnie przyda się AI w małej firmie?','Najczęściej do odpowiedzi na powtarzalne maile, opisów produktów, przygotowywania ofert i porządkowania danych. Na rozmowie powiemy wprost, gdzie AI ma sens, a gdzie wystarczy zwykła automatyzacja.'),
       ('Co, jeśli coś przestanie działać?','Po starcie poprawiamy to, co trzeba. Możemy też przejąć stałą opiekę nad automatyzacjami.'),
       ('Czy wystawiacie fakturę VAT?','Tak, jesteśmy polską spółką i wszystko jest na fakturę.')],
  final='Sprawdźmy, co w Twojej firmie może dziać się samo.'),
]

STEPS = [('Rozmowa','30 minut online. Mówisz, czego potrzebujesz.'),('Wycena','Dostajesz konkretną cenę i zakres na piśmie.'),('Wykonanie','Robimy, pokazujemy, poprawiamy razem z Tobą.'),('Start','Uruchamiamy i pokazujemy, jak z tego korzystać.')]

def page(p):
    s = []
    a = s.append
    canon = 'https://elok-agency.pl/' + p['slug'] + '/'
    a('<!doctype html><html lang="pl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">')
    a('<title>%s</title><meta name="description" content="%s"><link rel="canonical" href="%s">' % (e(p['title']), e(p['desc']), canon))
    a('<meta name="theme-color" content="#FFFFFF"><link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png"><link rel="apple-touch-icon" href="/apple-touch-icon.png">')
    a('<meta property="og:type" content="website"><meta property="og:locale" content="pl_PL"><meta property="og:site_name" content="ELOK"><meta property="og:title" content="%s"><meta property="og:description" content="%s"><meta property="og:url" content="%s"><meta property="og:image" content="https://elok-agency.pl/img/og.jpg">' % (e(p['title']), e(p['desc']), canon))
    a('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800&family=Figtree:wght@400;500;600&display=swap" rel="stylesheet">')
    a('<link rel="stylesheet" href="/lp.css?v=%s"></head><body class="light">' % V)
    a('<header class="lh" id="nav"><div class="w"><a class="logo" href="/" aria-label="ELOK, strona główna">ELOK<span>.</span></a><nav><a class="tel" href="tel:+48455505820"><small>Zadzwoń</small>455 505 820</a><a class="btn pri sm" href="#wycena">Bezpłatna wycena</a></nav></div></header>')
    a('<main>')
    # hero
    a('<section class="hero"><div class="w"><div>')
    a('<span class="eye">%s</span><h1>%s</h1><p class="lead">%s</p>' % (p['eye'], p['h1'], p['lead']))
    a('<div class="price"><b>%s</b><span>%s</span></div>' % p['price'])
    a('<ul class="ticks">' + ''.join('<li>%s<span>%s</span></li>' % (TICK, t) for t in p['ticks']) + '</ul>')
    a('<div class="ctas"><a class="btn pri" href="#wycena">Wycena w 24 godziny</a><a class="btn ghost" href="/konsultacja.html">Umów rozmowę online</a></div></div>')
    # form
    a('<div class="fcard" id="wycena"><h2>Bezpłatna wycena</h2><p class="s">Zostaw telefon albo e-mail. Odezwiemy się z wyceną w ciągu 24 godzin.</p>')
    a('<form id="lpform" data-zrodlo="%s" novalidate>' % p['zrodlo'])
    a('<label for="lp-co">Czego potrzebujesz?<select id="lp-co">' + ''.join('<option>%s</option>' % e(o) for o in p['co']) + '</select></label>')
    a('<label for="lp-imie">Imię<input id="lp-imie" autocomplete="name" placeholder="np. Marek" required></label>')
    a('<label for="lp-kontakt">Telefon lub e-mail<input id="lp-kontakt" autocomplete="tel" placeholder="np. 600 123 456 albo marek@firma.pl" required></label>')
    a('<input type="hidden" id="lp-firma" value=""><input type="text" id="lp-www2" class="hpf" tabindex="-1" autocomplete="off" aria-hidden="true">')
    a('<button class="btn gold" type="submit">Poproś o bezpłatną wycenę</button><div class="ferr" id="lperr" role="alert" hidden></div>')
    a('<p class="note">Wysyłając, zgadzasz się na kontakt w sprawie wyceny. Szczegóły: <a href="/polityka-prywatnosci.html">polityka prywatności</a>.</p></form>')
    a('<div class="fdone" id="lpdone">%s<h3>Dziękujemy, mamy Twoje zapytanie.</h3><p>Odezwiemy się w ciągu 24 godzin. Jeśli wolisz porozmawiać od razu, wybierz termin rozmowy.</p><a class="btn ghost" href="/konsultacja.html">Umów rozmowę online</a></div></div>' % TICK.replace('<svg ', '<svg style="width:54px;height:54px" '))
    a('</div></section>')
    # problemy
    a('<section class="s"><div class="w"><div class="sh"><small>Znasz to?</small><h2 class="t">Z czym przychodzą do nas firmy</h2></div><div class="g3">')
    for k, t, d in p['probs']:
        a('<div class="pc"><i>%s</i><h3>%s</h3><p>%s</p></div>' % (ic(k), t, d))
    a('</div></div></section>')
    # w cenie
    a('<section class="s alt"><div class="w"><div class="sh"><small>W cenie</small><h2 class="t">Co dostajesz</h2></div><div class="inc"><div class="incl"><ul>')
    a(''.join('<li>%s<span>%s</span></li>' % (TICK, t) for t in p['inc']))
    a('</ul></div><div class="pbox"><small>Cena</small><b>%s</b><p>%s</p><p>Bez ukrytych kosztów. Zakres i cenę dostajesz na piśmie przed startem.</p><a class="btn gold" href="#wycena">Poproś o wycenę</a></div></div></div></section>' % p['price'])
    # case
    ct, cd, flow, href, lab = p['case']
    a('<section class="s"><div class="w"><div class="sh"><small>Przykład</small><h2 class="t">Jak to wygląda w praktyce</h2></div><div class="case"><div class="ct"><h3>%s</h3><p>%s</p><a class="btn ghost sm" style="justify-self:start" href="/%s">%s</a></div><div class="cv"><div class="flow">' % (ct, cd, href, lab))
    a('<em>↓</em>'.join('<div>%s<span>%s</span></div>' % f for f in flow))
    a('</div></div></div></div></section>')
    # kroki
    a('<section class="s alt"><div class="w"><div class="sh"><small>Jak pracujemy</small><h2 class="t">Cztery proste kroki</h2></div><div class="steps">')
    for i, (t, d) in enumerate(STEPS):
        a('<div class="step"><small>0%d</small><b>%s</b><span>%s</span></div>' % (i + 1, t, d))
    a('</div></div></section>')
    # faq
    a('<section class="s"><div class="w"><div class="sh"><small>Pytania</small><h2 class="t">Najczęstsze pytania</h2></div><div class="faq">')
    for q, ans in p['faq']:
        a('<details><summary>%s</summary><p>%s</p></details>' % (q, ans))
    a('</div></div></section>')
    # final
    a('<section class="s" style="padding-top:0"><div class="w"><div class="final"><div><h2>%s</h2><p>Bezpłatnie i bez zobowiązań. Odpowiadamy w ciągu 24 godzin.</p></div><div class="ctas"><a class="btn gold" href="#wycena">Poproś o wycenę</a><a class="btn ghost" href="tel:+48455505820">455 505 820</a></div></div></div></section>' % p['final'])
    a('</main>')
    a('<footer class="lf"><div class="w"><span>© 2026 ELOK · polska spółka · faktura VAT</span><span><a href="/">elok-agency.pl</a> · <a href="/polityka-prywatnosci.html">Polityka prywatności</a> · <a href="/cookies.html">Cookies</a> · <a href="#" data-cookies>Ustawienia cookies</a></span></div></footer>')
    a('<div class="mbar"><a class="btn ghost" href="tel:+48455505820">Zadzwoń</a><a class="btn pri" href="#wycena">Bezpłatna wycena</a></div>')
    a('<script src="/ustawienia.js?v=%s"></script><script src="/site.js?v=%s"></script><script src="/lp.js?v=%s"></script></body></html>' % (V, V, V))
    return '\n'.join(s)

for p in PAGES:
    d = os.path.join(ROOT, p['slug'])
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w').write(page(p))
    print('ok', p['slug'])
