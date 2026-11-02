# Strona ELOK (elok-agency.pl)

Statyczna strona (HTML/CSS/JS), bez WordPressa.

- gałąź `test` → test.elok-agency.pl (niewidoczna dla Google, rezerwacja tylko udaje wysyłkę)
- gałąź `main` → elok-agency.pl – trafia tam dopiero po „Zatwierdź” w panelu (Aktualizacje)

Teksty i SEO zmieniane w panelu (Edytor strony) panel zapisuje od razu na serwerze i jako commit „Panel: …” na `main`.
Przed większymi zmianami zawsze najpierw pobierz aktualne `main` i scal z `test`.

`ustawienia.js` (identyfikatory Clarity, GA4, piksele) generuje panel na serwerze – nie ma go w repo.
`_zrodla/` – generator strony (Python), nie jest wgrywany na serwer.
