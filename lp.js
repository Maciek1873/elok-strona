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
/* Promocja dla pierwszych klientów: liczba miejsc i rabat ustawiane w panelu (Podłączenia), zapisywane w /ustawienia.js */
(function(){
 function run(c){
  var left=+c.promo||0,max=+c.promoMax||5,rab=+c.promoRabat||50;if(left<1||rab<1||rab>90)return;
  function fmt(n){n=Math.round(n);var s=String(n);return s.length>3?s.slice(0,-3)+' '+s.slice(-3):s;}
  function word(n){if(n===1)return 'Zostało 1 miejsce';var d=n%10,t=n%100;return (d>=2&&d<=4&&(t<12||t>14))?'Zostały '+n+' miejsca':'Zostało '+n+' miejsc';}
  var L=document.querySelectorAll('.price b,.pbox b');
  for(var i=0;i<L.length;i++){var b=L[i],m=b.textContent.match(/od\s*([\d\s ]+)\s*zł/);if(!m)continue;
   var n=parseInt(m[1].replace(/\D/g,''),10);if(!n)continue;
   b.innerHTML='od '+fmt(n*(100-rab)/100)+' zł <s class="lp-old">'+fmt(n)+' zł</s>';}
  var txt='<b>-'+rab+'% dla '+max+' pierwszych firm.</b> '+word(left)+'. W zamian prosimy o opinię w Google i zgodę na pokazanie realizacji.';
  var P=document.querySelectorAll('.hero .price,.pbox b');
  for(var j=0;j<P.length;j++){var d=document.createElement('div');d.className='lp-promo';d.innerHTML=txt;P[j].parentNode.insertBefore(d,P[j]);}
 }
 {try{var x=new XMLHttpRequest();x.open('GET','/ustawienia.js?n='+Date.now());x.onload=function(){var m=x.responseText.match(/ELOK_CFG=(\{.*\});/);if(m){try{run(JSON.parse(m[1]));}catch(e){}}};x.send();}catch(e){}}
})();
