/* Formularz szybkiej wyceny na landingach. Wysyła do panelu (Zgłoszenia + powiadomienie na telefon). Na wersji testowej tylko udaje wysyłkę. */
(function(){
 /* poprawki pod podkatalog: link w pasku cookies, pasek wersji testowej */
 [].forEach.call(document.querySelectorAll('.cookie a[href="cookies.html"]'),function(a){a.setAttribute('href','/cookies.html');});
 if(/^test\./.test(location.hostname)){var h=document.querySelector('.lh');if(h)h.style.top='32px';}
 /* klik w numer telefonu: zdarzenie w statystykach */
 document.addEventListener('click',function(e){var a=e.target.closest?e.target.closest('a[href^="tel:"]'):null;if(!a)return;try{if(window.gtag)gtag('event','klik_telefon');if(window.elokEv)elokEv('klik_telefon');}catch(x){}});
 var f=document.getElementById('lpform');if(!f)return;
 var API='https://panel.elok-agency.pl/strona/',LIVE=/^(www\.)?elok-agency\.pl$/.test(location.hostname);
 var err=document.getElementById('lperr'),done=document.getElementById('lpdone'),btn=f.querySelector('button[type=submit]'),t0=Math.floor(Date.now()/1000);
 var src=f.getAttribute('data-zrodlo')||'landing';
 function v(id){var e=document.getElementById(id);return e?e.value.trim():'';}
 function show(m){err.innerHTML=m;err.hidden=false;}
 function ok(){f.style.display='none';done.style.display='block';
  try{if(window.elokEv)elokEv('lead_'+src);if(window.elokKonwersja)elokKonwersja();}catch(e){}
  var y=done.getBoundingClientRect().top+(window.pageYOffset||0)-100;window.scrollTo(0,y);}
 f.addEventListener('submit',function(e){e.preventDefault();err.hidden=true;
  var req=[].filter.call(f.querySelectorAll('[required]'),function(i){return !i.value.trim();});if(req.length){req[0].focus();return;}
  var k=v('lp-kontakt'),isMail=/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(k),isTel=k.replace(/\D/g,'').length>=9;
  if(!isMail&&!isTel){show('Wpisz numer telefonu (9 cyfr) albo adres e-mail.');document.getElementById('lp-kontakt').focus();return;}
  if(!LIVE){ok();return;}
  var opis='[Landing: '+src+'] '+(v('lp-co')?'Temat: '+v('lp-co')+'. ':'')+(isTel&&!isMail?'Woli kontakt telefoniczny.':'');
  var data={a:'kontakt',imie:v('lp-imie'),email:isMail?k:'',telefon:isMail?'':k,firma:v('lp-firma'),opis:opis,www2:v('lp-www2'),ts:t0};
  var body=Object.keys(data).map(function(k){return encodeURIComponent(k)+'='+encodeURIComponent(data[k]);}).join('&');
  var old=btn.innerHTML;btn.disabled=true;btn.innerHTML='Wysyłam…';
  var x=new XMLHttpRequest();x.open('POST',API);x.setRequestHeader('Content-Type','application/x-www-form-urlencoded');x.timeout=20000;
  function fail(m){btn.disabled=false;btn.innerHTML=old;show(m||'Nie udało się wysłać. Spróbuj jeszcze raz albo zadzwoń: <a href="tel:+48455505820">455 505 820</a>.');}
  x.onload=function(){var r=null;try{r=JSON.parse(x.responseText);}catch(e){}if(r&&r.ok){ok();return;}fail(r&&r.error?r.error:null);};
  x.onerror=x.ontimeout=function(){fail();};x.send(body);});
})();
