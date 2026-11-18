# Podstrony SEO pod konkretne frazy. Uruchom: python3 _zrodla/seo_strony.py (potem python3 _zrodla/seo.py)
import re, html
src = open('realizacja-allegro.html', encoding='utf-8').read()
HEAD = src[:src.find('<main id="top">')]
FOOT = src[src.find('</main>'):]
FOOT = FOOT.replace('Sprzedajesz na Allegro? <span class="g">Pokażemy,</span> co da się zrobić samo.', 'Masz w firmie coś, co <span class="g">zjada czas?</span> Pokażemy, jak oddać to systemowi.')
CHK = '<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7"/></svg>'

P = [
dict(f='system-dla-serwisu-samochodowego.html', crumb='System dla serwisu samochodowego', img='img/okladka-serwis.jpg',
 title='System do wycen dla serwisu samochodowego · ELOK',
 desc='Program do wycen dla serwisu i warsztatu samochodowego: części z katalogu prosto do wyceny, aktualne ceny z hurtowni, oferta PDF mailem i faktura jednym kliknięciem.',
 tag='Dla serwisów i warsztatów samochodowych',
 h1='System do wycen <span class="g">dla serwisu samochodowego.</span>',
 lead='Doradca nie przepisuje już części z katalogu do programu, nie sprawdza cen u dostawcy i nie wpisuje tych samych pozycji drugi raz do faktury. Wycena robi się w kilka kliknięć, a klient dostaje ją od razu mailem.',
 kpis=[('−87%','czasu na przygotowanie wycen w serwisie, z którym pracujemy'),('0','ręcznie przepisywanych cen części'),('1 klik','i z wyceny robi się faktura')],
 prob_h='Gdzie serwis traci najwięcej czasu?',
 prob=['Doradca szuka części w programie katalogowym, a potem przepisuje numery i nazwy do programu z ofertami.','Ceny trzeba sprawdzać osobno w hurtowni, bo zmieniają się kilka razy w tygodniu.','Ofertę PDF i maila do klienta robi się ręcznie.','Po naprawie te same pozycje trafiają jeszcze raz do faktury.'],
 sol_h='Jak działa system?',
 sol=[('Część z katalogu jednym przyciskiem','W programie katalogowym klikasz „Wyślij do wyceny” i część razem z numerem trafia do systemu.'),('Ceny pobierają się same','System sprawdza aktualną cenę w hurtowni, a Ty ustawiasz tylko rabat i robociznę.'),('Oferta mailem albo linkiem','Klient dostaje czytelną ofertę z logo serwisu i PDF do pobrania.'),('Faktura z gotowej wyceny','Po naprawie zamieniasz wycenę w fakturę jednym kliknięciem, bez przepisywania.')],
 case=('realizacja-serwis.html','Case study: od katalogu części do faktury bez przepisywania','Z 10 godzin do 1 h 18 min tygodniowo na wyceny w serwisie premium.'),
 price='Automatyzacje i systemy zaczynają się od 600 zł netto. Cenę całego systemu dla serwisu podajemy po bezpłatnej rozmowie, zawsze przed startem prac.',
 faq=[('Czy muszę zmieniać program katalogowy albo księgowy?','Nie. System łączymy z programami, których serwis już używa, i przejmuje tylko te kroki, które dziś robi się ręcznie.'),('Czy to działa dla małego warsztatu?','Tak. System dopasowujemy do liczby stanowisk i sposobu pracy. Przy kilku wycenach dziennie oszczędność czasu też jest wyraźna.'),('Ile trwa wdrożenie?','Zależy od tego, z iloma programami i hurtowniami trzeba się połączyć. Termin podajemy przed startem prac.'),('Czy zespół da sobie radę z obsługą?','Projektujemy ekrany tak, żeby obsługa była prosta także dla osób, które nie lubią komputera. Po starcie przygotowujemy instrukcję i poprawiamy to, co przeszkadza.')]),
dict(f='automatyzacja-allegro.html', crumb='Automatyzacja Allegro', img='img/allegro/okladka.jpg',
 title='Automatyzacja sprzedaży na Allegro i aplikacja do ofert · ELOK',
 desc='Aplikacja do wystawiania ofert na Allegro z telefonu: skan numeru części, dane z katalogu Allegro, etykiety z kodem QR, zamówienia i wiadomości w jednym miejscu.',
 tag='Dla firm sprzedających na Allegro',
 h1='Automatyzacja sprzedaży <span class="g">na Allegro.</span>',
 lead='Budujemy indywidualne aplikacje, które skracają wystawianie ofert, pilnują zamówień i wiadomości od kupujących oraz łączą Allegro z magazynem, drukarką i fakturami.',
 kpis=[('1 skan','aparat telefonu czyta numer części, bez przepisywania'),('z katalogu','tytuł i parametry uzupełniają się z katalogu Allegro'),('QR','etykieta na każdym produkcie prowadzi prosto do oferty')],
 prob_h='Co zjada czas przy sprzedaży na Allegro?',
 prob=['Zdjęcia trzeba przerzucać z telefonu na komputer.','Numery katalogowe i parametry przepisuje się ręcznie, a literówka oznacza ofertę, której nikt nie znajdzie.','Zamówienia, wiadomości i kończące się oferty trzeba sprawdzać w kilku miejscach.','Przy sprzedaży trzeba szukać na magazynie, który to produkt.'],
 sol_h='Co może robić aplikacja?',
 sol=[('Wystawianie z telefonu','Zdjęcia, numer, stan i cena. Oferta trafia na Twoje konto Allegro.'),('Opisy według szablonu','Opis dopasowuje się sam, np. do stanu produktu: nowy, używany albo uszkodzony.'),('Etykiety z kodem QR','Na każdy produkt drukuje się naklejka, a przy zamówieniu od razu wiadomo, co zdjąć z półki.'),('Zamówienia, wiadomości, powiadomienia','Wszystko w jednym miejscu, z powiadomieniem na telefon o każdej sprzedaży i pytaniu.')],
 case=('realizacja-allegro.html','Case study: część na Allegro w minutę, prosto z telefonu','Indywidualna aplikacja dla serwisu sprzedającego używane części.'),
 price='Automatyzacje zaczynają się od 600 zł netto. Każdą aplikację projektujemy pod konkretną firmę, cenę podajemy po bezpłatnej rozmowie.',
 faq=[('Czy to gotowa aplikacja do pobrania?','Nie. Każde wdrożenie budujemy pod konkretną firmę: jej konto Allegro, produkty, drukarkę i sposób pracy.'),('Czy aplikacja jest zgodna z zasadami Allegro?','Tak. Łączy się przez oficjalne API Allegro, a Ty logujesz się swoim kontem i sam dajesz dostęp.'),('Czy działa dla innych produktów niż części samochodowe?','Tak. Ten sam schemat sprawdzi się przy odzieży, elektronice czy towarze z magazynu.'),('Czy da się połączyć Allegro z fakturami i wysyłką?','Tak. Zamówienia mogą tworzyć dokumenty sprzedaży i etykiety przewoźników, zależnie od tego, z czego korzystasz.')]),
dict(f='integracja-sklepu-z-hurtownia.html', crumb='Integracja sklepu z hurtownią', img='img/okladka-sklep.jpg',
 title='Integracja sklepu internetowego z hurtownią · ELOK',
 desc='Integracja sklepu z hurtownią: ceny i stany aktualizowane co noc, zamówienia prosto do panelu, etykiety kurierskie i dokumenty sprzedaży automatycznie.',
 tag='Dla sklepów internetowych',
 h1='Integracja sklepu <span class="g">z hurtownią.</span>',
 lead='Łączymy sklep internetowy z hurtownią lub dostawcą, żeby ceny i dostępność aktualizowały się same, a zamówienia, wysyłki i dokumenty nie wymagały przepisywania.',
 kpis=[('co noc','ceny i stany całego katalogu aktualizują się same'),('1 panel','zamówienia, klienci, wysyłki i dokumenty'),('1 klik','i etykieta kurierska drukuje się sama')],
 prob_h='Kiedy sklep potrzebuje integracji?',
 prob=['Hurtownia często zmienia ceny i stany, a Ty pilnujesz ich ręcznie.','Klient zamawia produkt, którego już nie ma u dostawcy.','Każde zamówienie trzeba osobno wpisać u dostawcy.','Etykiety, paragony i faktury robi się w kilku programach.'],
 sol_h='Co obejmuje integracja?',
 sol=[('Katalog z hurtowni','Co noc system sprawdza ceny i dostępność każdego produktu i aktualizuje sklep.'),('Zamówienia w panelu','Każde zamówienie trafia od razu do panelu, gotowe do zamówienia u dostawcy.'),('Wysyłka jednym kliknięciem','Etykieta kurierska drukuje się sama, a klient dostaje maile ze statusem przesyłki.'),('Dokumenty automatycznie','Paragon albo faktura powstają po doręczeniu, razem z dokumentem przyjęcia towaru.')],
 case=('realizacja-sklep.html','Case study: sklep, który sam pilnuje cen, stanów i dokumentów','Sklep z oryginalnymi częściami BMW i MINI połączony z hurtownią.'),
 price='Sklep internetowy zaczyna się od 1 800 zł netto, integracje od 600 zł netto. Dokładną cenę podajemy po bezpłatnej rozmowie.',
 faq=[('Z jakimi hurtowniami da się połączyć sklep?','Z każdą, która udostępnia API, plik z cenami (CSV, XML) albo panel B2B. Sprawdzamy to na bezpłatnej rozmowie.'),('Czy muszę zmieniać platformę sklepu?','Nie zawsze. Często integrujemy istniejący sklep, np. na WooCommerce. Jeśli platforma ogranicza rozwój, doradzimy nową.'),('Co, jeśli hurtownia zmieni ceny w ciągu dnia?','Częstotliwość aktualizacji ustawiamy pod dostawcę: co noc, co kilka godzin albo częściej dla stanów.'),('Czy integracja obejmie też Allegro?','Tak, sklep i Allegro mogą korzystać z tych samych cen i stanów.')]),
dict(f='strona-dla-warsztatu-samochodowego.html', crumb='Strona dla warsztatu samochodowego', img='img/okladka-serwis.jpg',
 title='Strona internetowa dla warsztatu samochodowego · ELOK',
 desc='Strona dla warsztatu i serwisu samochodowego, z której klient od razu dzwoni: telefon na pierwszym ekranie, ceny usług, formularz wyceny i dobra widoczność w Google.',
 tag='Dla warsztatów i serwisów samochodowych',
 h1='Strona dla warsztatu, <span class="g">z której klient dzwoni.</span>',
 lead='Klient szuka warsztatu z telefonu, często, gdy auto już się zepsuło. Robimy strony, na których w kilka sekund widzi, co naprawiacie, ile to kosztuje i jak się umówić.',
 kpis=[('od 800 zł','netto za stronę firmową z formularzem'),('1 klik','do telefonu z każdego ekranu'),('Google','SEO lokalne pod Twoje miasto i usługi')],
 prob_h='Dlaczego strona warsztatu nie przynosi telefonów?',
 prob=['Na telefonie pierwszy ekran to zdjęcie i hasło, a numer trzeba szukać.','Brak cen, więc klient dzwoni do konkurencji, która je podaje.','Nie widać, czy warsztat jest teraz otwarty.','Strona nie wyświetla się w Google na hasła z nazwą miasta.'],
 sol_h='Co dostaje warsztat?',
 sol=[('Telefon na pierwszym ekranie','Numer i przycisk „Zostaw numer” od razu, a na telefonie stały pasek „Zadzwoń”.'),('Ceny najczęstszych usług','Przegląd, diagnostyka, wymiana opon. Klient dzwoni już zdecydowany.'),('Formularz wyceny','Zgłoszenie trafia od razu na maila albo do panelu warsztatu.'),('Widoczność w Google','Osobne podstrony usług, dane dla Google i wizytówka w mapach.')],
 case=('realizacja-serwis.html','Zobacz też: system wycen dla serwisu samochodowego','Strona może przekazywać zgłoszenia prosto do systemu serwisu.'),
 price='Strona firmowa zaczyna się od 800 zł netto. Do strony możemy dołożyć system wycen i przypomnienia dla klientów.',
 faq=[('Czy strona będzie dobrze wyglądać na telefonie?','Tak, projektujemy ją najpierw pod telefon, bo stamtąd przychodzi większość klientów warsztatu.'),('Czy sam zmienię ceny i godziny otwarcia?','Tak, ceny, teksty i oferty sezonowe zmienisz w prostym panelu, bez programisty.'),('Czy pomożecie z wizytówką Google?','Tak, ustawimy wizytówkę i podstrony usług tak, żeby warsztat wyświetlał się na hasła z nazwą miasta.'),('Ile trwa zrobienie strony?','Zależy od liczby podstron i tego, czy masz zdjęcia. Termin podajemy przed startem prac.')]),
dict(f='dedykowany-system-dla-firmy.html', crumb='Dedykowany system dla firmy', img='img/okladka-panel.jpg',
 title='Dedykowany system dla firmy, program na zamówienie · ELOK',
 desc='Dedykowany system dla firmy: oferty, klienci, zamówienia, faktury i raporty w jednym panelu, zbudowanym pod Twój sposób pracy i połączonym z programami, których używasz.',
 tag='Systemy szyte na miarę',
 h1='Dedykowany system <span class="g">dla Twojej firmy.</span>',
 lead='Gdy gotowe programy nie pasują do sposobu, w jaki pracujesz, budujemy panel na zamówienie: oferty, klienci, zamówienia, faktury i raporty w jednym miejscu.',
 kpis=[('1 panel','zamiast kilku programów i arkuszy'),('Twoje procesy','system dopasowany do firmy, nie odwrotnie'),('od 600 zł','netto za pierwsze automatyzacje')],
 prob_h='Kiedy warto zbudować własny system?',
 prob=['Dane są w kilku programach i Excelu, a te same rzeczy wpisuje się wielokrotnie.','Gotowy program wymaga obejść, bo nie pasuje do branży.','Właściciel nie ma jednego miejsca, w którym widzi wyniki firmy.','Firma rośnie, a ręcznej pracy przybywa szybciej niż ludzi.'],
 sol_h='Co może zawierać system?',
 sol=[('Oferty i klienci','Oferty PDF, historia klienta i przypomnienia w jednym miejscu.'),('Zamówienia i magazyn','Statusy zamówień, stany i zamówienia u dostawców.'),('Faktury i rozliczenia','Dokumenty sprzedaży, raport kasowy i podatki liczone osobno dla każdej marki.'),('Raporty i powiadomienia','Najważniejsze liczby na maila rano i powiadomienia o tym, co wymaga uwagi.')],
 case=('realizacja-panel.html','Case study: panel finansowy dla dwóch marek w jednej spółce','Raport kasowy, oferty i podatki dla dwóch sklepów w jednym panelu.'),
 price='Proste automatyzacje zaczynają się od 600 zł netto. Cenę systemu podajemy po bezpłatnej rozmowie, zawsze przed rozpoczęciem pracy.',
 faq=[('Czy dedykowany system jest drogi?','Nie musi. Zaczynamy od jednego procesu, który zjada najwięcej czasu, i rozbudowujemy system etapami.'),('Czy system połączy się z moimi programami?','W większości przypadków tak: z księgowością, sklepem, Allegro, hurtowniami czy pocztą.'),('Co, jeśli coś trzeba będzie zmienić?','System rozwijamy razem z firmą. Nowe funkcje dokładamy, kiedy pojawia się potrzeba.'),('Kto jest właścicielem systemu?','Twoja firma. Dane należą do Ciebie, a zasady korzystania z systemu zapisujemy w umowie.')]),
dict(f='strony-internetowe-konstancin-piaseczno.html', crumb='Konstancin-Jeziorna i Piaseczno', img='img/allegro/okladka.jpg',
 title='Strony internetowe i automatyzacje: Konstancin, Piaseczno · ELOK',
 desc='ELOK z Konstancina-Jeziorny: strony internetowe, sklepy i automatyzacje dla firm z Konstancina, Piaseczna, Warszawy i okolic. Cała współpraca online, bez dojazdów.',
 tag='Konstancin-Jeziorna · Piaseczno · Warszawa',
 h1='Strony i automatyzacje <span class="g">z Konstancina-Jeziorny.</span>',
 lead='Jesteśmy firmą z Konstancina-Jeziorny. Budujemy strony internetowe, sklepy i systemy dla firm z Konstancina, Piaseczna, Warszawy i okolic, a z resztą Polski pracujemy online.',
 kpis=[('lokalnie','firma z Konstancina-Jeziorny, blisko Piaseczna i Warszawy'),('od 800 zł','netto za stronę firmową'),('od 600 zł','netto za automatyzacje')],
 prob_h='Z czym przychodzą do nas lokalne firmy?',
 prob=['Strona nie przynosi telefonów albo nie wyświetla się w Google na nazwę miasta.','Oferty, faktury i zamówienia zajmują godziny ręcznej pracy.','Sklep wymaga pilnowania cen i stanów u dostawcy.','Reklamy w Google kosztują, a zapytań nie przybywa.'],
 sol_h='W czym pomagamy?',
 sol=[('Strony internetowe','Szybkie strony z telefonem na pierwszym ekranie i formularzem wyceny.'),('Sklepy internetowe','Płatności, wysyłki i połączenie z hurtownią albo Allegro.'),('Automatyzacje i systemy','Panele, oferty, faktury i integracje szyte pod firmę.'),('Lokalne SEO i reklamy','Wizytówka Google, podstrony pod miasta i kampanie mierzone telefonami.')],
 case=('realizacje.html','Zobacz nasze realizacje','Aplikacja do Allegro, system wycen, sklep z częściami i panel finansowy.'),
 price='Strony od 800 zł netto, sklepy od 1 800 zł netto, automatyzacje od 600 zł netto. Pierwsza rozmowa jest bezpłatna.',
 faq=[('Czy trzeba się spotykać?','Nie. Rozmowa, projekt i odbiór odbywają się online, więc nie tracisz czasu na dojazdy.'),('Czy pracujecie tylko z firmami z okolicy?','Nie, pracujemy z firmami z całej Polski. Dobrze znamy jednak lokalny rynek Konstancina, Piaseczna i południowej Warszawy.'),('Czy pomożecie z widocznością w Google w moim mieście?','Tak, przygotujemy podstrony usług, dane dla Google i wizytówkę w mapach.'),('Ile kosztuje strona dla lokalnej firmy?','Strona firmowa z formularzem zaczyna się od 800 zł netto. Dokładną cenę podajemy po rozmowie.')]),
]

def page(p):
    h = HEAD
    h = re.sub(r'<title>.*?</title>', '<title>' + p['title'] + '</title>', h, count=1, flags=re.S)
    for k in ('name="description"', 'property="og:description"'):
        h = re.sub(r'(<meta ' + k + r' content=")[^"]*', lambda m: m.group(1) + html.escape(p['desc']), h, count=1)
    h = re.sub(r'(<meta property="og:title" content=")[^"]*', lambda m: m.group(1) + html.escape(p['title']), h, count=1)
    h = h.replace('realizacja-allegro.html', p['f']).replace('img/allegro/okladka.jpg', p['img'])
    kp = ''.join(f'<div class="rv"><b>{a}</b><span>{b}</span></div>' for a, b in p['kpis'])
    prob = ''.join(f'<li>{x}</li>' for x in p['prob'])
    sol = ''.join(f'<div><b>{a}</b><p>{b}</p></div>' for a, b in p['sol'])
    faq = ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in p['faq'])
    cu, ct, cd = p['case']
    m = f'''<main id="top"><section class="phero"><div class="wrap"><div class="crumbs"><a href="index.html">Strona główna</a> / {p['crumb']}</div><span class="tagbig" style="display:inline-flex;gap:10px;font-weight:700;font-size:15px;padding:8px 16px;border-radius:999px;background:rgba(207,168,94,.14);color:var(--gold)">{p['tag']}</span><h1 style="max-width:18ch">{p['h1']}</h1><p class="lead">{p['lead']}</p>
<div class="btns" style="margin-top:28px"><a class="btn pri mag" href="konsultacja.html">Umów bezpłatną konsultację <span class="ar">→</span></a><a class="btn sec" href="cennik.html">Zobacz cennik</a></div>
<div class="kpis">{kp}</div></div></section>
<section class="band"><div class="wrap split"><div class="prose rv"><div class="eyebrow">Problem</div><h2 style="margin:12px 0 22px">{p['prob_h']}</h2><ul style="padding-left:20px;display:grid;gap:10px;color:var(--mut);font-size:17.5px">{prob}</ul></div>
<a class="ct rv" href="{cu}" style="align-self:center"><div class="th"><img src="{p['img']}" alt="{html.escape(ct)}" loading="lazy" style="object-position:center"></div><div class="bd"><span class="tg">Realizacja</span><h3>{ct}</h3><p>{cd}</p></div></a></div></section>
<section><div class="wrap split"><div class="rv"><div class="eyebrow">Rozwiązanie</div><h2 style="margin:12px 0 10px">{p['sol_h']}</h2><div class="tline">{sol}</div></div>
<div class="prose rv"><div class="eyebrow">Cena</div><h3 style="margin:12px 0 14px">Ile to kosztuje?</h3><p>{p['price']}</p><div class="btns" style="margin-top:22px"><a class="btn pri mag" href="konsultacja.html">Zapytaj o wycenę <span class="ar">→</span></a></div></div></div></section>
<section><div class="wrap narrow"><div class="shead rv"><div><div class="eyebrow">Pytania</div><h2>Najczęstsze pytania</h2></div></div><div class="faq">{faq}</div></div></section>'''
    open(p['f'], 'w', encoding='utf-8').write(h + m + FOOT)
    print('ok', p['f'])

for p in P: page(p)
