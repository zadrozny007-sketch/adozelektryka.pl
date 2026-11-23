import json, os
# Generator strony adozelektryka.pl. Uruchom: python3 _narzedzia/build.py
# Zapisuje gotowe pliki HTML w głównym folderze repozytorium.
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = "https://adozelektryka.pl"
TEL = "511 933 675"; TEL_H = "+48511933675"
WA = "https://wa.me/48511933675"
WA_NUM = "48511933675"
MAIL = "adozelektryka@gmail.com"
ADDR = "ul. Pilawska 11, 08-445 Osieck"
GMAPS = "https://www.google.com/maps/search/?api=1&query=AdoZ+Auto+Elektryk+Samochodowy+Osieck"
REVIEWS = "https://www.google.com/search?q=AdoZ+Auto+Elektryk+Samochodowy+Osieck"

ICON_PHONE = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg>'
MARK = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#4fe3b0" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 13h4l2-6 3 12 3-9 2 3h6"/></svg>'

# Opinie z Google, wpisane dosłownie: (autor, liczba gwiazdek, treść). Bez dat.
OPINIE = []

def karuzela():
    if not OPINIE: return ""
    import html as _h
    cards = "".join(
        '<figure class="rv-card"><div class="rv-stars" aria-label="%d na 5 gwiazdek">%s</div>'
        '<blockquote><p>%s</p></blockquote><figcaption>%s</figcaption></figure>'
        % (g, "★"*g, _h.escape(t).replace("\n","</p><p>"), _h.escape(a)) for a, g, t in OPINIE)
    return ('<div class="rv" data-rv><div class="rv-track" tabindex="0" aria-label="Opinie klientów z Google">' + cards +
            '</div><div class="rv-nav"><button type="button" class="rv-btn" data-rv-prev aria-label="Poprzednie opinie">←</button>'
            '<button type="button" class="rv-btn" data-rv-next aria-label="Następne opinie">→</button></div></div>')

NAV = [("diagnostyka-komputerowa.html","Diagnostyka"),("elektryka-samochodowa.html","Elektryka"),("klucze-samochodowe.html","Klucze"),("sterowniki-i-moduly.html","Sterowniki"),("naprawa-adblue-dpf-egr.html","AdBlue i DPF"),("kontakt.html","Kontakt")]

TOWNS = ["Osieck","Pilawa","Sobienie-Jeziory","Celestynów","Kołbiel","Wilga","Parysów","Garwolin","Siennica","Karczew","Otwock","Józefów","Góra Kalwaria","Łaskarzew","Maciejowice","Mińsk Mazowiecki"]
TOWNS_TXT = "Pilawy, Sobień-Jezior, Celestynowa, Kołbieli, Wilgi, Parysowa, Garwolina, Siennicy, Karczewa, Otwocka, Józefowa, Góry Kalwarii, Łaskarzewa, Maciejowic i Mińska Mazowieckiego"
BRANDS = ["Volkswagen","Audi","Skoda","Seat","Cupra","Ford","Peugeot","Citroën","Opel","Fiat","Jeep","Renault","Dacia","Toyota","Hyundai","Kia","BMW","Mercedes","Volvo","Nissan","Mazda","Honda"]

SCHEMA = {
 "@context":"https://schema.org","@type":"AutoRepair","name":"AdoZ Auto — Elektryk Samochodowy Osieck",
 "url":DOMAIN+"/","telephone":TEL_H,"email":MAIL,
 "address":{"@type":"PostalAddress","streetAddress":"Pilawska 11","postalCode":"08-445","addressLocality":"Osieck","addressRegion":"mazowieckie","addressCountry":"PL"},
 "openingHoursSpecification":[
   {"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"08:00","closes":"18:00"},
   {"@type":"OpeningHoursSpecification","dayOfWeek":"Saturday","opens":"09:00","closes":"15:00"}],
 "areaServed":TOWNS
}

def head(title, desc, path, extra=""):
    canon = DOMAIN + "/" + ("" if path=="index.html" else path)
    return f'''<!doctype html>
<html lang="pl" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website">
<meta property="og:locale" content="pl_PL">
<meta property="og:site_name" content="AdoZ Auto">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{DOMAIN}/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="AdoZ Auto, elektryk samochodowy w Osiecku, tel. 511 933 675">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#14251f">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="style.css">
<script type="application/ld+json">{json.dumps(SCHEMA, ensure_ascii=False)}</script>
{extra}</head>
<body>
<a class="skip" href="#tresc">Przejdź do treści</a>
'''

def header(path):
    cur = ' aria-current="page"'
    links = "".join('<a href="%s"%s>%s</a>' % (h, cur if h==path else "", t) for h,t in NAV)
    return f'''<div class="topbar"><div class="wrap">
<span>Tel. <a href="tel:{TEL_H}">{TEL}</a></span>
<span>{ADDR}</span>
<span>pon.–pt. 8:00–18:00, sob. 9:00–15:00</span>
</div></div>
<header class="site-header"><div class="wrap">
<a class="brand" href="./"><span class="brand-mark">{MARK}</span><span><span class="brand-name">AdoZ Auto</span><span class="brand-sub">Elektryk samochodowy w Osiecku</span></span></a>
<button class="nav-toggle" aria-expanded="false" aria-controls="nav">Menu</button>
<nav class="nav" id="nav" aria-label="Główne menu">{links}</nav>
<a class="btn btn-dark header-call" href="tel:{TEL_H}">{ICON_PHONE}{TEL}</a>
</div></header>
<main id="tresc">
'''

def footer():
    return f'''</main>
<footer class="site-footer"><div class="wrap">
<div class="cols">
<div>
<h2>AdoZ Auto</h2>
<p>Elektryk samochodowy i diagnostyka komputerowa w Osiecku. Auta wszystkich marek. Przyjeżdżają do nas kierowcy z {TOWNS_TXT}.</p>
</div>
<div>
<h2>Usługi</h2>
<ul>
<li><a href="diagnostyka-komputerowa.html">Diagnostyka komputerowa i oscyloskopowa</a></li>
<li><a href="elektryka-samochodowa.html">Elektryka samochodowa</a></li>
<li><a href="elektronika-moduly.html">Elektronika i moduły sterujące</a></li>
<li><a href="klucze-samochodowe.html">Klucze samochodowe</a></li>
<li><a href="sterowniki-i-moduly.html">Sterowniki silnika i moduły</a></li>
<li><a href="vag-diagnostyka-i-kodowanie.html">VW, Audi, Skoda, Seat</a></li>
<li><a href="ford-diagnostyka-i-programowanie.html">Ford</a></li>
<li><a href="stellantis-diagnostyka-i-programowanie.html">Peugeot, Citroën, Opel, Fiat</a></li>
<li><a href="naprawa-adblue-dpf-egr.html">Naprawa AdBlue, DPF i EGR</a></li>
<li><a href="chiptuning.html">Chiptuning</a></li>
<li><a href="dla-warsztatow.html">Dla warsztatów</a></li>
</ul>
</div>
<div>
<h2>Kontakt</h2>
<ul>
<li><a href="tel:{TEL_H}">{TEL}</a></li>
<li><a href="{WA}">WhatsApp</a></li>
<li><a href="mailto:{MAIL}">{MAIL}</a></li>
<li>{ADDR}</li>
<li>pon.–pt. 8:00–18:00<br>sobota 9:00–15:00</li>
</ul>
</div>
</div>
<div class="legal">AdoZ Auto Dawid Zadrożny, NIP 532-211-71-53. <a href="polityka-prywatnosci.html">Polityka prywatności</a></div>
</div></footer>
<div class="callbar"><a class="btn btn-wire" href="tel:{TEL_H}">{ICON_PHONE}Zadzwoń</a><a class="btn btn-dark" href="kontakt.html#zgloszenie">Zgłoś usterkę</a></div>
<script src="main.js"></script>
</body>
</html>
'''

CALLBACK = f'''<form class="callback" id="cb-form" data-wa="{WA_NUM}" novalidate>
<h2>Nie możesz się dodzwonić?</h2>
<p>Zostaw numer. Otworzy się SMS albo WhatsApp z gotową prośbą o telefon, a my oddzwonimy w godzinach pracy.</p>
<div class="field"><label for="cb-imie">Imię</label><input id="cb-imie" type="text" name="imie" autocomplete="given-name"></div>
<div class="field"><label for="cb-tel">Telefon</label><input id="cb-tel" type="tel" name="telefon" autocomplete="tel" inputmode="tel"></div>
<p class="form-error" role="alert"></p>
<div class="send-btns"><button class="btn btn-dark" type="submit" name="kanal" value="sms">Wyślij SMS</button><button class="btn btn-line" type="submit" name="kanal" value="wa">WhatsApp</button></div>
<p class="form-note">Wiadomość wysyłasz sam ze swojego telefonu. Strona niczego nie zapisuje.</p>
</form>'''

def chips(name, items):
    return '<div class="chips">' + "".join(f'<label class="chip"><input type="checkbox" name="{name}" value="{i}"><span>{i}</span></label>' for i in items) + '</div>'

def radios(name, items):
    return '<div class="chips">' + "".join(f'<label class="chip"><input type="radio" name="{name}" value="{i}"><span>{i}</span></label>' for i in items) + '</div>'

TICKET = f'''<form class="ticket" id="ticket-form" data-wa="{WA_NUM}" novalidate>
<div class="progress" aria-hidden="true"><span></span><span></span><span></span></div>

<fieldset class="fs">
<legend class="step-title">Jakie to auto?</legend>
<p class="step-sub">Krok 1 z 3</p>
<div class="grid2">
<div class="field"><label for="t-marka">Marka i model</label><input id="t-marka" type="text" name="marka" placeholder="np. Volkswagen Passat B7"></div>
<div class="field"><label for="t-rok">Rok produkcji</label><input id="t-rok" type="text" name="rok" inputmode="numeric" placeholder="np. 2013"></div>
<div class="field"><label for="t-silnik">Silnik <span class="hint">(jeśli wiesz)</span></label><input id="t-silnik" type="text" name="silnik" placeholder="np. 2.0 TDI"></div>
<div class="field"><label for="t-vin">VIN <span class="hint">(opcjonalnie)</span></label><input id="t-vin" type="text" name="vin" maxlength="17" placeholder="17 znaków z dowodu"></div>
</div>
</fieldset>

<fieldset class="fs" hidden>
<legend class="step-title">Co się dzieje z autem?</legend>
<p class="step-sub">Krok 2 z 3. Zaznacz wszystko, co pasuje.</p>
{chips("objawy[]", ["Nie odpala","Nie kręci rozrusznik","Rozładowuje akumulator","Świeci kontrolka","Brak komunikacji z modułem","Gaśnie w trakcie jazdy","Tryb awaryjny","Nie działa oświetlenie","Nie działa licznik","Nie działa centralny zamek","Błędy wracają po skasowaniu","Błąd AdBlue lub DPF","Potrzebny klucz","Wymiana sterownika"])}
<p class="legend">Kiedy występuje?</p>
{radios("kiedy", ["Cały czas","Na zimno","Na ciepło","Po deszczu","Raz na jakiś czas"])}
<p class="legend">Czy auto jeździ?</p>
{radios("jezdzi", ["Tak, dojadę","Nie, trzeba holować"])}
<div class="field"><label for="t-opis">Opisz problem własnymi słowami</label><textarea id="t-opis" name="opis" placeholder="Co się dzieje, od kiedy, co już było robione i gdzie"></textarea></div>
</fieldset>

<fieldset class="fs" hidden>
<legend class="step-title">Jak się z Tobą skontaktować?</legend>
<p class="step-sub">Krok 3 z 3. Na końcu otworzy się SMS albo WhatsApp z gotową wiadomością. Wystarczy ją wysłać.</p>
<div class="grid2">
<div class="field"><label for="t-imie">Imię</label><input id="t-imie" type="text" name="imie" autocomplete="given-name"></div>
<div class="field"><label for="t-tel">Telefon <span class="hint">(jeśli inny niż ten, z którego piszesz)</span></label><input id="t-tel" type="tel" name="telefon" autocomplete="tel" inputmode="tel"></div>
</div>
<p class="legend">Kiedy najlepiej dzwonić?</p>
{radios("pora", ["Rano","W południe","Po południu","Obojętnie"])}
<p class="form-note">Wiadomość wysyłasz sam ze swojego telefonu. Strona niczego nie zapisuje. <a href="polityka-prywatnosci.html">Polityka prywatności</a></p>
</fieldset>

<p class="form-error" role="alert"></p>
<div class="step-nav">
<button class="btn btn-line" type="button" data-back>Wstecz</button>
<button class="btn btn-dark" type="button" data-next>Dalej</button>
<div class="send-btns" data-send hidden><button class="btn btn-wire" type="submit" name="kanal" value="sms">Wyślij SMS</button><button class="btn btn-dark" type="submit" name="kanal" value="wa">WhatsApp</button></div>
</div>
</form>'''

TRACE = '<svg class="trace" viewBox="0 0 1200 120" preserveAspectRatio="none" aria-hidden="true"><path d="M0 70 H140 L150 70 L158 22 L166 108 L174 70 H330 C350 70 352 40 372 40 S394 100 414 100 S436 40 456 40 S478 100 498 100 S520 70 540 70 H640 V28 H700 V100 H760 V28 H820 V100 H880 V70 H1010 L1020 70 L1028 22 L1036 108 L1044 70 H1200"/></svg>'

def write(name, html):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f: f.write(html)

def ico(path):
    return f'<span class="ico"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#4fe3b0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{path}</svg></span>'

I_DIAG = '<rect x="3" y="4" width="18" height="13" rx="2"/><path d="M6 12h3l1.5-3 2 5 1.5-2H18M8 21h8"/>'
I_ELEC = '<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>'
I_KEY = '<circle cx="7.5" cy="15.5" r="4.5"/><path d="M10.7 12.3 21 2M17 6l3 3M14 9l2 2"/>'
I_GAS = '<path d="M3 17h4c2 0 2-3 4-3s2 3 4 3 2-3 4-3h2M3 11h4c2 0 2-3 4-3s2 3 4 3 2-3 4-3h2"/>'
I_TUNE = '<path d="M4 18a8 8 0 1 1 16 0"/><path d="M12 18l4-6"/><circle cx="12" cy="18" r="1.4"/>'
I_SHOP = '<path d="M3 21V9l9-6 9 6v12M8 21v-6h8v6"/>'
I_MOD = '<rect x="5" y="5" width="14" height="14" rx="2"/><path d="M9 1v4M15 1v4M9 19v4M15 19v4M1 9h4M1 15h4M19 9h4M19 15h4"/>'

# ---------- index ----------
index = head("Elektryk samochodowy Osieck — diagnostyka komputerowa | AdoZ Auto",
  "Elektryk samochodowy w Osiecku. Diagnostyka komputerowa i oscyloskopowa, usterki instalacji elektrycznej, brak komunikacji modułów. Pilawa, Kołbiel, Otwock, Garwolin.","index.html") + header("index.html") + f'''
<section class="hero"><div class="wrap">
<div>
<h1>Elektryk samochodowy w Osiecku</h1>
<p class="lead">Szukamy przyczyny usterki, zamiast kasować błędy. Diagnostyka komputerowa i oscyloskopowa, instalacja elektryczna, moduły sterujące, sterowniki i klucze. Samochody wszystkich marek.</p>
<div class="hero-actions">
<a class="btn btn-wire" href="tel:{TEL_H}">{ICON_PHONE}Zadzwoń: {TEL}</a>
<a class="btn btn-line" href="#zgloszenie">Opisz usterkę</a>
</div>
<ul class="hero-facts">
<li><strong>5,0 ★</strong> w opiniach Google</li>
<li><strong>Wszystkie marki</strong> aut osobowych</li>
<li><strong>Pn–pt</strong> 8–18, <strong>sob.</strong> 9–15</li>
</ul>
</div>
{CALLBACK}
</div>{TRACE}</section>

<section><div class="wrap">
<div class="section-head"><h2>Czym się zajmujemy</h2><p>Elektryka i elektronika to dziś większość usterek w autach. To nasza specjalizacja.</p></div>
<div class="services">
<a class="service" href="diagnostyka-komputerowa.html">{ico(I_DIAG)}<h3>Diagnostyka komputerowa i oscyloskopowa</h3><p>Odczyt błędów to początek. Sprawdzamy parametry pracy na żywo i mierzymy sygnały czujników oscyloskopem.</p><span class="more">Więcej o diagnostyce</span></a>
<a class="service" href="elektryka-samochodowa.html">{ico(I_ELEC)}<h3>Elektryka samochodowa</h3><p>Rozładowujący się akumulator, zwarcia, przerwy w wiązkach, ładowanie, rozruch, oświetlenie.</p><span class="more">Więcej o elektryce</span></a>
<a class="service" href="elektronika-moduly.html">{ico(I_MOD)}<h3>Elektronika i moduły sterujące</h3><p>Brak komunikacji z modułem, błędy magistrali CAN, kontrolki ABS, ESP i poduszek, usterki sterowników.</p><span class="more">Więcej o elektronice</span></a>
</div>
</div></section>


<section class="alt"><div class="wrap">
<div class="section-head"><h2>Usługi specjalistyczne</h2><p>Rzeczy, z którymi nie każdy warsztat sobie poradzi. Przed przyjazdem zadzwoń i podaj model auta, powiemy, czy możemy pomóc.</p></div>
<div class="services">
<a class="service" href="klucze-samochodowe.html">{ico(I_KEY)}<h3>Klucze i immobilizery</h3><p>Zapasowy klucz i pilot, klucze bezkluczykowe. Także gdy zgubiłeś wszystkie klucze.</p><span class="more">Więcej o kluczach</span></a>
<a class="service" href="sterowniki-i-moduly.html">{ico(I_MOD)}<h3>Sterowniki silnika i moduły</h3><p>Używany sterownik i auto nie odpala? Klonowanie sterowników silnika, skrzyni, BSI i BCM.</p><span class="more">Więcej o sterownikach</span></a>
<a class="service" href="vag-diagnostyka-i-kodowanie.html">{ico(I_DIAG)}<h3>VAG, Ford i Stellantis</h3><p>Diagnostyka, kodowanie i programowanie w oprogramowaniu producenta, online. VW, Audi, Skoda, Seat, Ford, Peugeot, Citroën, Opel, Fiat, Jeep.</p><span class="more">Więcej o VAG</span></a>
<a class="service" href="naprawa-adblue-dpf-egr.html">{ico(I_GAS)}<h3>Naprawa AdBlue, DPF i EGR</h3><p>Błędy układu SCR, pompa AdBlue, regeneracja i czyszczenie filtra DPF.</p><span class="more">Więcej o naprawie</span></a>
<a class="service" href="chiptuning.html">{ico(I_TUNE)}<h3>Chiptuning</h3><p>Zmiana oprogramowania sterownika na sprawnym aucie, z kopią oryginału.</p><span class="more">Więcej o chiptuningu</span></a>
<a class="service" href="dla-warsztatow.html">{ico(I_SHOP)}<h3>Dla warsztatów</h3><p>Przejmujemy trudne usterki, sterowniki, klucze i kodowanie. Sterowniki można przysłać kurierem.</p><span class="more">Współpraca</span></a>
</div>
<div class="brands-box"><h3>Naprawiamy auta wszystkich marek</h3><p>Grupa VW, Ford i Stellantis w oprogramowaniu producenta, online: <a href="vag-diagnostyka-i-kodowanie.html">VAG</a>, <a href="ford-diagnostyka-i-programowanie.html">Ford</a>, <a href="stellantis-diagnostyka-i-programowanie.html">Stellantis</a>. Pozostałe marki testerami wielomarkowymi i pomiarami. Przy nietypowym modelu zadzwoń wcześniej.</p>
<ul class="brands">{"".join("<li>%s</li>" % b for b in BRANDS)}<li>i inne</li></ul></div>
</div></section>
<section><div class="wrap">
<div class="section-head"><h2>Z czym najczęściej przyjeżdżają do nas kierowcy</h2><p>Jeśli rozpoznajesz swój problem, zadzwoń. Większość z tych usterek ma przyczynę w instalacji, którą da się zmierzyć.</p></div>
<ul class="symptoms">
<li><strong>Auto nie odpala albo nie kręci rozrusznik</strong><span>Rozruch, zasilanie, immobilizer, masy</span></li>
<li><strong>Akumulator rozładowuje się na postoju</strong><span>Pobór prądu przez moduł, który nie przechodzi w uśpienie</span></li>
<li><strong>Świecą kontrolki ABS, ESP lub poduszek</strong><span>Czujniki, wtyczki, przewody, sterowniki</span></li>
<li><strong>Brak komunikacji z modułem</strong><span>Błędy typu U, magistrala CAN, zasilanie modułu</span></li>
<li><strong>Auto gaśnie lub wchodzi w tryb awaryjny</strong><span>Czujniki, sygnały, zakłócenia w instalacji</span></li>
<li><strong>Błędy wracają po skasowaniu</strong><span>Znak, że przyczyna nie została usunięta</span></li>
<li><strong>Nie działa licznik, oświetlenie lub centralny zamek</strong><span>Moduły komfortu, wiązki, przekaźniki</span></li>
<li><strong>Usterka pojawia się raz na jakiś czas</strong><span>Najtrudniejsze przypadki, do wyszukania pomiarami</span></li>
</ul>
</div></section>

<section class="alt"><div class="wrap">
<div class="section-head"><h2>Jak wygląda naprawa</h2><p>Najpierw ustalamy przyczynę, potem rozmawiamy o naprawie.</p></div>
<ol class="steps">
<li><h3>Opisujesz problem</h3><p>Telefonicznie albo przez formularz. Ustalamy termin przyjazdu.</p></li>
<li><h3>Diagnozujemy</h3><p>Odczyt błędów, parametry na żywo, pomiary oscyloskopem i miernikiem.</p></li>
<li><h3>Uzgadniamy zakres</h3><p>Mówimy, co jest uszkodzone i ile będzie kosztować naprawa. Decyzja należy do Ciebie.</p></li>
<li><h3>Naprawiamy i sprawdzamy</h3><p>Po naprawie ponowny test, żeby mieć pewność, że usterka nie wróci.</p></li>
</ol>
</div></section>

<section><div class="wrap">
<div class="section-head"><h2>Dlaczego AdoZ Auto</h2></div>
<div class="reasons">
<div><h3>Diagnoza oparta na pomiarach</h3><p>Nie wymieniamy części na próbę. Sprawdzamy sygnały i przewody, zanim cokolwiek zamówimy.</p></div>
<div><h3>Zakres i koszt przed naprawą</h3><p>O tym, co robimy, decydujesz Ty, po rozmowie z nami.</p></div>
<div><h3>Wszystkie marki</h3><p>Grupę VW, Forda i Stellantis (Peugeot, Citroën, Opel, Fiat, Jeep) obsługujemy w oprogramowaniu producenta, online. Pozostałe marki testerami wielomarkowymi.</p></div>
<div><h3>Otwarte także w soboty</h3><p>Od poniedziałku do piątku 8:00–18:00, w sobotę 9:00–15:00.</p></div>
</div>
</div></section>

<section class="alt"><div class="wrap">
<div class="reviews">
<div><div class="score">5,0 <span class="stars" aria-label="5 na 5 gwiazdek">★★★★★</span></div><p>Średnia ocen naszych klientów w Google</p></div>
<div class="btns"><a class="btn btn-wire" href="{REVIEWS}" rel="noopener" target="_blank">Zobacz opinie w Google</a></div>
</div>
{karuzela()}
</div></section>

<section id="zgloszenie"><div class="wrap">
<div class="section-head"><h2>Opisz usterkę</h2><p>Trzy krótkie kroki. Im więcej szczegółów, tym szybciej powiemy, czy i kiedy możemy pomóc.</p></div>
{TICKET}
</div></section>

<section class="alt"><div class="wrap contact-grid">
<div>
<div class="section-head"><h2>Gdzie jesteśmy</h2></div>
<ul class="contact-list">
<li><span class="k">Telefon</span><a href="tel:{TEL_H}">{TEL}</a></li>
<li><span class="k">Adres</span><a href="{GMAPS}" target="_blank" rel="noopener">{ADDR}</a></li>
</ul>
<table class="hours"><caption class="hp">Godziny otwarcia</caption>
<tr><td>Poniedziałek–piątek</td><td>8:00–18:00</td></tr>
<tr><td>Sobota</td><td>9:00–15:00</td></tr>
<tr><td>Niedziela</td><td>nieczynne</td></tr></table>
</div>
<iframe class="map" title="Mapa dojazdu do AdoZ Auto" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=51.9662741,21.4246991&z=16&output=embed"></iframe>
</div></section>
''' + footer()
write("index.html", index)

# ---------- service pages ----------
def aside():
    return f'''<aside class="aside"><h2>Masz taki problem?</h2><p>Zadzwoń albo opisz usterkę. Oddzwonimy i ustalimy termin.</p>
<a class="btn btn-wire" href="tel:{TEL_H}">{ICON_PHONE}{TEL}</a>
<a class="btn btn-dark" href="kontakt.html#zgloszenie">Opisz usterkę</a>
<a class="btn btn-line" href="{WA}">Napisz na WhatsApp</a></aside>'''

def service(path, title, desc, h1, lead, body, crumb):
    html = head(title, desc, path) + header(path) + f'''
<section class="page-hero"><div class="wrap">
<div class="crumbs"><a href="./">Strona główna</a> / {crumb}</div>
<h1>{h1}</h1><p>{lead}</p>
<a class="btn btn-wire" href="tel:{TEL_H}">{ICON_PHONE}Zadzwoń: {TEL}</a>
</div></section>
<section><div class="wrap layout"><article class="prose">{body}</article>{aside()}</div></section>
''' + footer()
    write(path, html)

service("diagnostyka-komputerowa.html",
 "Diagnostyka komputerowa i oscyloskopowa Osieck | AdoZ Auto",
 "Diagnostyka komputerowa samochodu w Osiecku. Odczyt błędów, parametry na żywo i pomiary oscyloskopem. Szukamy przyczyny, nie kasujemy błędów. Pilawa, Kołbiel, Otwock.",
 "Diagnostyka komputerowa i oscyloskopowa",
 "Kod błędu mówi, gdzie sterownik zauważył problem. Nie mówi, co jest uszkodzone. Dlatego na odczycie błędów się nie kończymy.",
 """<h2>Na czym polega diagnostyka</h2>
<p>Każde auto zaczynamy od podłączenia testera i odczytu błędów ze wszystkich dostępnych modułów, nie tylko z silnika. To daje obraz całości: często usterka w jednym miejscu wywołuje błędy w kilku innych.</p>
<p>Potem sprawdzamy, co faktycznie się dzieje:</p>
<ul>
<li><strong>Parametry na żywo.</strong> Odczyty czujników w trakcie pracy silnika lub jazdy, porównane z wartościami, które powinny być.</li>
<li><strong>Pomiary oscyloskopem.</strong> Kształt sygnału z czujnika lub elementu wykonawczego. Tester pokazuje tylko liczbę, oscyloskop pokazuje, czy sygnał jest prawidłowy.</li>
<li><strong>Pomiary instalacji.</strong> Zasilanie, masy, spadki napięć, ciągłość przewodów i stan wtyczek.</li>
</ul>
<h2>Dlaczego samo kasowanie błędów nie pomaga</h2>
<p>Skasowany błąd wraca, jeśli przyczyna została w aucie. Zdarza się też, że wymiana części wskazanej przez kod nic nie daje, bo winny był przewód albo wtyczka prowadząca do tej części. Pomiar pozwala tego uniknąć i nie płacić za części, które były sprawne.</p>
<h2>Kiedy warto przyjechać na diagnostykę</h2>
<ul>
<li>świeci kontrolka silnika, ABS, ESP lub poduszek powietrznych,</li>
<li>auto traci moc, szarpie lub przechodzi w tryb awaryjny,</li>
<li>błędy wracają po skasowaniu,</li>
<li>usterka pojawia się tylko czasem, na zimno, na ciepło albo po deszczu,</li>
<li>inny warsztat wymienił części, a problem został.</li>
</ul>
<h2>Częste pytania</h2>
<details><summary>Ile trwa diagnostyka?</summary><p>Zależy od usterki. Odczyt i wstępna ocena idą szybko. Usterki, które pojawiają się tylko czasami, wymagają dłuższych pomiarów. Przed rozpoczęciem mówimy, czego się spodziewać.</p></details>
<details><summary>Czy po diagnostyce muszę naprawiać auto u Was?</summary><p>Nie. Dostajesz informację, co jest uszkodzone. Decyzja o naprawie należy do Ciebie.</p></details>
<details><summary>Czy trzeba się wcześniej umówić?</summary><p>Tak, najlepiej zadzwonić. Ustalimy termin, żeby auto nie czekało.</p></details>""",
 "Diagnostyka komputerowa")

service("elektryka-samochodowa.html",
 "Elektryk samochodowy Osieck — naprawa instalacji elektrycznej | AdoZ Auto",
 "Elektryk samochodowy w Osiecku. Rozładowujący się akumulator, problemy z rozruchem i ładowaniem, zwarcia i przerwy w wiązkach, oświetlenie. Okolice Pilawy, Kołbieli i Otwocka.",
 "Elektryk samochodowy w Osiecku",
 "Rozruch, ładowanie, zasilanie, wiązki, oświetlenie. Szukamy usterki pomiarami, zamiast wymieniać części na próbę.",
 """<h2>Czym się zajmujemy</h2>
<ul>
<li><strong>Rozruch i ładowanie.</strong> Auto nie kręci, kręci słabo albo akumulator nie jest doładowywany w trakcie jazdy.</li>
<li><strong>Rozładowujący się akumulator.</strong> Szukamy odbiornika, który pobiera prąd na postoju, na przykład modułu, który nie przechodzi w uśpienie.</li>
<li><strong>Wiązki i wtyczki.</strong> Przetarte przewody, korozja w złączach, przerwy i zwarcia, także po wcześniejszych naprawach i montażu dodatkowych urządzeń.</li>
<li><strong>Zasilanie i masy.</strong> Słabe połączenia masowe potrafią wywołać zupełnie przypadkowe objawy w wielu układach naraz.</li>
<li><strong>Oświetlenie i wyposażenie.</strong> Światła, szyby, lusterka, centralny zamek, ogrzewanie szyb i foteli.</li>
</ul>
<h2>Jak szukamy usterki</h2>
<p>Zaczynamy od schematu instalacji i pomiarów: napięcia, spadki napięć, rezystancja, pobór prądu. Dzięki temu wiemy, w którym miejscu obwodu jest problem, zanim zaczniemy rozbierać auto.</p>
<h2>Kiedy warto przyjechać</h2>
<ul>
<li>akumulator pada po kilku dniach postoju,</li>
<li>po deszczu albo myjni coś przestaje działać,</li>
<li>kilka niezwiązanych rzeczy psuje się naraz,</li>
<li>bezpieczniki przepalają się ponownie.</li>
</ul>
<h2>Częste pytania</h2>
<details><summary>Czy nowy akumulator rozwiąże problem z rozładowaniem?</summary><p>Jeśli coś pobiera prąd na postoju, nowy akumulator też się rozładuje. Najpierw warto zmierzyć pobór prądu.</p></details>
<details><summary>Czy naprawiacie instalację po montażu alarmu, haka lub radia?</summary><p>Tak. To częsta przyczyna usterek, bo dodatkowe urządzenie zostało wpięte w instalację w nieodpowiednim miejscu.</p></details>""",
 "Elektryka samochodowa")

service("elektronika-moduly.html",
 "Brak komunikacji z modułem, błędy CAN — elektronika samochodowa Osieck | AdoZ Auto",
 "Brak komunikacji z modułem, błędy magistrali CAN, kontrolki ABS, ESP i poduszek. Diagnostyka elektroniki samochodowej w Osiecku. Okolice Otwocka, Pilawy i Garwolina.",
 "Elektronika i moduły sterujące",
 "Brak komunikacji z modułem, błędy magistrali CAN, kontrolki ABS, ESP i poduszek. Usterki, których nie da się znaleźć samym odczytem błędów.",
 """<h2>Brak komunikacji z modułem</h2>
<p>Komunikat „brak komunikacji” albo błędy typu U oznaczają, że sterowniki w aucie przestały się ze sobą porozumiewać. Przyczyną najczęściej nie jest sam moduł, tylko jego zasilanie, masa, przewody magistrali CAN albo wtyczka. Sprawdzamy to pomiarami, zanim ktokolwiek zamówi drogi sterownik.</p>
<h2>Magistrala CAN</h2>
<p>Przez magistralę CAN rozmawiają ze sobą sterowniki silnika, skrzyni, ABS, licznika i wyposażenia. Jedno uszkodzone urządzenie albo przetarty przewód potrafi zakłócić pracę całej sieci. Oscyloskop pokazuje, czy sygnał na magistrali jest prawidłowy i gdzie szukać przyczyny.</p>
<h2>Z czym jeszcze przyjeżdżają klienci</h2>
<ul>
<li>kontrolki ABS, ESP i poduszek powietrznych, które nie gasną,</li>
<li>licznik, który gaśnie, pokazuje bzdury albo traci podświetlenie,</li>
<li>auto, które nie odpala, choć rozrusznik i paliwo są w porządku,</li>
<li>sterowniki po zalaniu wodą lub po przepięciu.</li>
</ul>
<h2>Częste pytania</h2>
<details><summary>Czy moduł trzeba wymienić na nowy?</summary><p>Często nie. Najpierw sprawdzamy zasilanie, masy i przewody. Dopiero gdy one są w porządku, przyczyną może być sam sterownik.</p></details>
<details><summary>Czy da się naprawić auto po zalaniu?</summary><p>To zależy od tego, które elementy zostały zalane i jak długo. Trzeba obejrzeć i zmierzyć instalację.</p></details>""",
 "Elektronika i moduły")

# ---------- usługi specjalistyczne ----------
service("klucze-samochodowe.html",
 "Dorabianie kluczy samochodowych Osieck, także po zgubieniu wszystkich | AdoZ Auto",
 "Zapasowy klucz i pilot, klucze bezkluczykowe, programowanie immobilizera. Także gdy zgubiłeś wszystkie klucze. Osieck, Pilawa, Otwock, Garwolin.",
 "Klucze samochodowe i immobilizery",
 "Zapasowy klucz, nowy pilot, klucz bezkluczykowy. Pomagamy także wtedy, gdy zgubiłeś wszystkie klucze do auta.",
 """<h2>Co robimy</h2>
<ul>
<li><strong>Zapasowy klucz i pilot.</strong> Programujemy nowy klucz do auta, zanim zgubisz jedyny, który masz.</li>
<li><strong>Wszystkie klucze zgubione.</strong> Auto nie ma żadnego działającego klucza, a trzeba je uruchomić.</li>
<li><strong>Klucze bezkluczykowe (keyless).</strong> Auta otwierane i uruchamiane bez wkładania klucza.</li>
<li><strong>Usunięcie zgubionego klucza z pamięci auta.</strong> Żeby zgubiony lub skradziony klucz przestał uruchamiać samochód, tam gdzie auto na to pozwala.</li>
<li><strong>Immobilizer po wymianie sterownika.</strong> Odczyt kodu PIN i dopasowanie immobilizera, gdy wymieniony został sterownik silnika lub moduł.</li>
<li><strong>Naprawa pilotów.</strong> Przyciski, obudowy, styki.</li>
</ul>
<h2>Jakie auta</h2>
<p>Większość marek samochodów osobowych, także nowsze roczniki. Możliwości zależą od konkretnego modelu i rocznika, dlatego przed przyjazdem zadzwoń i podaj markę, model i rok. Powiemy od razu, czy i jak możemy pomóc.</p>
<h2>Klucz robimy tylko właścicielowi</h2>
<p>Przy każdym zleceniu sprawdzamy dowód rejestracyjny auta i dowód osobisty. Jeśli auto nie jest zarejestrowane na Ciebie, potrzebne będzie upoważnienie właściciela.</p>
<h2>Częste pytania</h2>
<details><summary>Co zabrać ze sobą?</summary><p>Dowód rejestracyjny, dowód osobisty i wszystkie klucze do auta, które masz, także te uszkodzone.</p></details>
<details><summary>Dlaczego trzeba przywieźć wszystkie klucze?</summary><p>W wielu autach programowanie nowego klucza usuwa z pamięci te, których nie było przy programowaniu. Klucz, którego zabraknie, może przestać działać.</p></details>
<details><summary>Zgubiłem wszystkie klucze. Jak dowieźć auto?</summary><p>Auto bez klucza trzeba przywieźć na lawecie. Zadzwoń najpierw, ustalimy, czy Twój model da się zrobić i kiedy.</p></details>""",
 "Klucze samochodowe")

service("sterowniki-i-moduly.html",
 "Klonowanie sterownika silnika, skrzyni i BSI Osieck | AdoZ Auto",
 "Wymieniłeś sterownik na używany i auto nie odpala? Klonowanie sterowników silnika i skrzyni, także DSG, oraz modułów BSI i BCM. Kopia oprogramowania, odzyskiwanie sterowników.",
 "Sterowniki silnika, skrzyni i moduły",
 "Wymieniłeś sterownik na używany i auto nie odpala? Przenosimy oprogramowanie i dane immobilizera do sterownika zamiennego, żeby auto działało jak przed awarią.",
 """<h2>Klonowanie sterownika silnika i skrzyni</h2>
<p>Używany sterownik z innego auta ma w sobie oprogramowanie i dane immobilizera tamtego auta. Dlatego po zwykłej wymianie silnik często nie odpala. Klonowanie przenosi do sterownika zamiennego wszystko, co było w oryginalnym. Robimy to dla sterowników silnika i skrzyni biegów, także DSG.</p>
<p>Nie każdy sterownik da się sklonować. Zanim kupisz używany, wyślij nam zdjęcie naklejki z oboma numerami, ze starego i z nowego. Powiemy, czy to zadziała.</p>
<h2>Moduły BSI, BCM i licznik</h2>
<p>To samo dotyczy modułów elektroniki nadwozia, na przykład BSI w Peugeocie i Citroënie. Przy wymianie modułu przenosimy immobilizer, zaprogramowane klucze i ustawienia auta.</p>
<p>Przy wymianie licznika przenosimy do zamiennego rzeczywisty przebieg ze starego. Nie zmieniamy przebiegu. Po wymianie licznika właściciel ma 14 dni na zgłoszenie się na stację kontroli pojazdów.</p>
<h2>Co jeszcze robimy</h2>
<ul>
<li><strong>Kopia zapasowa oprogramowania</strong> przed każdą ingerencją w sterownik.</li>
<li><strong>Odczyt i zapis</strong> przez gniazdo diagnostyczne, a gdy się nie da, po wyjęciu sterownika z auta.</li>
<li><strong>Odzyskanie sterownika</strong>, który przestał działać po nieudanym programowaniu.</li>
<li><strong>Przywrócenie oryginalnego oprogramowania</strong>, gdy jest dostępny właściwy plik.</li>
<li><strong>Odczyt danych z uszkodzonego modułu</strong>, jeśli jego pamięć jest sprawna.</li>
<li><strong>Sterowniki poduszek powietrznych po kolizji.</strong></li>
<li><strong>Naprawa płytek elektroniki</strong>, lutowanie uszkodzonych elementów.</li>
</ul>
<h2>Nie tylko samochody osobowe</h2>
<p>Sterowniki z motocykli, samochodów ciężarowych, ciągników, łodzi i quadów. Możliwości zależą od konkretnego sterownika, dlatego najpierw podaj jego numer.</p>
<h2>Częste pytania</h2>
<details><summary>Czy muszę przyjechać autem?</summary><p>Nie zawsze. Przy klonowaniu często wystarczą oba sterowniki. Warsztaty mogą je przysłać kurierem, opis jest na stronie <a href="dla-warsztatow.html">Dla warsztatów</a>.</p></details>
<details><summary>Ile to trwa?</summary><p>Zależy od sterownika. Po numerze powiemy, czego się spodziewać.</p></details>""",
 "Sterowniki i moduły")

service("vag-diagnostyka-i-kodowanie.html",
 "Diagnostyka i kodowanie VW, Audi, Skoda, Seat Osieck | AdoZ Auto",
 "Diagnostyka, kodowanie i adaptacje Volkswagena, Audi, Skody i Seata w oprogramowaniu producenta, także online. Kodowanie po wymianie części i doposażeniu. Osieck, Otwock, Garwolin.",
 "Diagnostyka i kodowanie VW, Audi, Skoda, Seat",
 "Pracujemy na oprogramowaniu producenta, także w trybie online. To samo narzędzie diagnostyczne, z którego korzysta serwis marki.",
 """<h2>Diagnostyka</h2>
<p>Odczyt wszystkich sterowników w aucie i prowadzone wyszukiwanie usterek przygotowane przez producenta, krok po kroku, z pomiarami. Do tego oscyloskop, gdy trzeba sprawdzić sam sygnał.</p>
<h2>Kodowanie i adaptacje</h2>
<ul>
<li><strong>Po wymianie części.</strong> Nowy lub używany sterownik, moduł, licznik, lampa czy czujnik często nie zadziała bez kodowania.</li>
<li><strong>Doposażenie.</strong> Włączenie funkcji po montażu nowego wyposażenia.</li>
<li><strong>Nastawy podstawowe.</strong> Przepustnica, skrzynia DSG i automatyczna, zawór EGR, zawieszenie.</li>
<li><strong>Kodowanie poduszek powietrznych</strong> po wymianie elementów.</li>
<li><strong>Aktualizacje oprogramowania sterowników.</strong></li>
</ul>
<h2>Nowsze roczniki</h2>
<p>W nowszych autach grupy VW, mniej więcej od rocznika 2020, sterowniki są zabezpieczone przed zmianami. Żeby je zakodować, trzeba najpierw odblokować dostęp przez serwer producenta. Robimy to.</p>
<h2>Częste pytania</h2>
<details><summary>Czy zrobicie wszystko, co serwis marki?</summary><p>Większość. Kilka funkcji wymaga uprawnień, które producent daje tylko swoim serwisom, na przykład zdjęcie ochrony komponentów. Zadzwoń i powiedz, co trzeba zrobić. Powiemy przed przyjazdem.</p></details>
<details><summary>Czy kodujecie inne marki?</summary><p>Tak. Fordy obsługujemy w oprogramowaniu producenta online, więcej na stronie <a href="ford-diagnostyka-i-programowanie.html">Ford</a>. Marki Stellantis, czyli Peugeota, Citroëna, Opla, Fiata i Jeepa, również w oprogramowaniu producenta, więcej na stronie <a href="stellantis-diagnostyka-i-programowanie.html">Stellantis</a>. Pozostałe marki kodujemy po wymianie modułu, zakres zależy od marki i rocznika.</p></details>""",
 "VW, Audi, Skoda, Seat")

service("naprawa-adblue-dpf-egr.html",
 "Naprawa AdBlue (SCR), DPF i EGR Osieck | AdoZ Auto",
 "Błąd AdBlue, odliczanie do braku rozruchu, zapchany filtr DPF, błędy EGR. Naprawa układu SCR, adaptacja pompy AdBlue, regeneracja i czyszczenie DPF. Osieck, Otwock, Garwolin.",
 "Naprawa AdBlue (SCR), DPF i EGR",
 "Błąd AdBlue i odliczanie do braku rozruchu, zapchany filtr cząstek stałych, kontrolka silnika od zaworu EGR. Przywracamy sprawność układu.",
 """<h2>AdBlue i układ SCR</h2>
<p>Gdy układ AdBlue zgłasza usterkę, auto zaczyna odliczać kilometry, po których nie da się go uruchomić. Nie warto czekać do zera.</p>
<ul>
<li><strong>Diagnostyka układu SCR.</strong> Sprawdzamy dozowanie, grzanie i czujniki, żeby wymienić tylko to, co jest uszkodzone.</li>
<li><strong>Naprawa układu SCR.</strong></li>
<li><strong>Adaptacja nowej pompy AdBlue</strong> po wymianie, żeby sterownik ją rozpoznał i układ zaczął działać.</li>
</ul>
<h2>Filtr DPF</h2>
<ul>
<li><strong>Regeneracja.</strong> Wymuszone wypalenie sadzy z filtra testerem, gdy auto nie zdołało zrobić tego samo w trakcie jazdy.</li>
<li><strong>Czyszczenie (pranie) filtra DPF</strong>, gdy regeneracja już nie wystarcza.</li>
<li><strong>Diagnostyka przyczyny.</strong> Filtr zapycha się najczęściej z jakiegoś powodu: czujnik różnicy ciśnień, wtryskiwacze, krótkie trasy. Bez usunięcia przyczyny problem wróci.</li>
</ul>
<h2>Zawór EGR</h2>
<p>Diagnostyka zaworu i jego sterowania, nastawy po wymianie.</p>
<h2>Częste pytania</h2>
<details><summary>Ile mogę jeszcze przejechać z błędem AdBlue?</summary><p>Tyle, ile pokazuje licznik na desce. Po dojściu do zera auto może nie odpalić. Zadzwoń, zanim do tego dojdzie.</p></details>
<details><summary>Czy po naprawie auto przejdzie przegląd?</summary><p>Naprawiamy układy tak, żeby działały, jak przewidział producent.</p></details>""",
 "Naprawa AdBlue, DPF i EGR")

service("ford-diagnostyka-i-programowanie.html",
 "Diagnostyka i programowanie Ford online Osieck | AdoZ Auto",
 "Diagnostyka Forda w oprogramowaniu producenta online. Programowanie i aktualizacje sterowników, konfiguracja modułu po wymianie. Osieck, Otwock, Garwolin.",
 "Diagnostyka i programowanie Ford",
 "Fordy obsługujemy w oprogramowaniu producenta, online. Diagnostyka, programowanie sterowników i aktualizacje oprogramowania.",
 """<h2>Co robimy</h2>
<ul>
<li><strong>Diagnostyka</strong> wszystkich sterowników w oprogramowaniu producenta.</li>
<li><strong>Programowanie sterowników</strong> przez serwer Forda.</li>
<li><strong>Aktualizacje oprogramowania</strong> sterowników.</li>
<li><strong>Moduł po wymianie.</strong> Nowy lub używany moduł w Fordzie często nie zadziała, dopóki nie zostanie zaprogramowany i skonfigurowany pod konkretne auto.</li>
</ul>
<h2>Kiedy warto przyjechać</h2>
<ul>
<li>wymieniony moduł nie działa albo zgłasza błąd konfiguracji,</li>
<li>usterka, którą producent usuwa aktualizacją oprogramowania,</li>
<li>błędy, których zwykły tester nie potrafi wyjaśnić.</li>
</ul>
<h2>Częste pytania</h2>
<details><summary>Czy obsługujecie każdy model Forda?</summary><p>Zależy od modelu i rocznika. Zadzwoń i podaj model, rok i co trzeba zrobić.</p></details>""",
 "Ford")

service("stellantis-diagnostyka-i-programowanie.html",
 "Diagnostyka i programowanie Peugeot, Citroën, Opel, Fiat online Osieck | AdoZ Auto",
 "Peugeot, Citroën, DS, Opel, Fiat, Alfa Romeo, Jeep w oprogramowaniu producenta Stellantis, online. Diagnostyka, programowanie i aktualizacje sterowników, konfiguracja modułów po wymianie. Osieck, Otwock, Garwolin.",
 "Diagnostyka i programowanie Stellantis",
 "Peugeot, Citroën, DS, Opel, Fiat, Alfa Romeo, Lancia i Jeep. Pracujemy w oprogramowaniu producenta, online, przez interfejs pass-thru.",
 """<h2>Co robimy</h2>
<ul>
<li><strong>Diagnostyka</strong> wszystkich sterowników w oprogramowaniu producenta.</li>
<li><strong>Programowanie sterowników</strong> przez serwer Stellantis.</li>
<li><strong>Aktualizacje oprogramowania</strong> sterowników.</li>
<li><strong>Moduł po wymianie.</strong> Nowy lub używany sterownik, BSI czy BCM często nie zadziała, dopóki nie zostanie zaprogramowany i skonfigurowany pod konkretne auto.</li>
</ul>
<h2>Kiedy warto przyjechać</h2>
<ul>
<li>wymieniony moduł nie działa albo zgłasza błąd konfiguracji,</li>
<li>usterka, którą producent usuwa aktualizacją oprogramowania,</li>
<li>błędy, których zwykły tester nie potrafi wyjaśnić.</li>
</ul>
<h2>Częste pytania</h2>
<details><summary>Czy obsługujecie każdy model?</summary><p>Zależy od modelu i rocznika. Zadzwoń i podaj markę, model, rok i co trzeba zrobić.</p></details>
<details><summary>A inne marki?</summary><p>Grupę VW i Forda też obsługujemy w oprogramowaniu producenta: <a href="vag-diagnostyka-i-kodowanie.html">VW, Audi, Skoda, Seat</a> i <a href="ford-diagnostyka-i-programowanie.html">Ford</a>. Pozostałe marki diagnozujemy testerami wielomarkowymi i pomiarami.</p></details>""",
 "Stellantis")

service("chiptuning.html",
 "Chiptuning Osieck, Otwock, Garwolin | AdoZ Auto",
 "Chiptuning, czyli zmiana oprogramowania sterownika silnika. Kopia oryginalnego oprogramowania przed zmianą, możliwość powrotu do ustawień seryjnych. Osieck i okolice.",
 "Chiptuning",
 "Więcej mocy i momentu obrotowego przez zmianę oprogramowania sterownika silnika. Na sprawnym aucie, z kopią oryginału.",
 """<h2>Jak to wygląda</h2>
<ol>
<li><strong>Diagnostyka.</strong> Najpierw sprawdzamy stan auta. Chiptuningu nie robimy na aucie z usterką, bo zmiana oprogramowania jej nie naprawi, a może ją pogłębić.</li>
<li><strong>Kopia oryginału.</strong> Odczytujemy i zapisujemy oryginalne oprogramowanie sterownika.</li>
<li><strong>Zmiana oprogramowania.</strong> Wgrywamy zmodyfikowane oprogramowanie dopasowane do silnika.</li>
<li><strong>Sprawdzenie.</strong> Po zmianie sprawdzamy pracę silnika i błędy.</li>
</ol>
<h2>Na co zwrócić uwagę</h2>
<p>Chiptuning robimy na sprawnym aucie, z działającymi układami oczyszczania spalin. Zmiana mocy może mieć znaczenie dla gwarancji i ubezpieczenia, dlatego warto to sprawdzić przed decyzją.</p>
<h2>Częste pytania</h2>
<details><summary>Czy da się wrócić do oryginalnego oprogramowania?</summary><p>Tak. Przed zmianą zapisujemy kopię oryginału.</p></details>
<details><summary>Ile mocy przybędzie?</summary><p>To zależy od silnika i jego stanu. Zadzwoń i podaj model, rok i silnik.</p></details>""",
 "Chiptuning")

service("dla-warsztatow.html",
 "Dla warsztatów: sterowniki, klucze, kodowanie, trudne usterki | AdoZ Auto",
 "Współpraca z warsztatami: trudne usterki elektryczne, klonowanie sterowników i modułów, klucze, kodowanie VAG, Ford i Stellantis. Sterowniki można przysłać kurierem.",
 "Dla warsztatów",
 "Trudna usterka elektryczna, sterownik, klucz albo kodowanie, którego nie robicie u siebie? Przyjmujemy zlecenia od innych warsztatów.",
 """<h2>Co możemy przejąć</h2>
<ul>
<li><strong>Trudne usterki elektryczne</strong>: brak komunikacji, magistrala CAN, usterki pojawiające się czasami.</li>
<li><strong>Sterowniki silnika i skrzyni</strong>: klonowanie, odczyt i zapis, odzyskiwanie po nieudanym programowaniu.</li>
<li><strong>Moduły</strong>: BSI, BCM, licznik, odczyt pamięci, naprawa płytek.</li>
<li><strong>Klucze i immobilizery.</strong></li>
<li><strong>Kodowanie i programowanie VW, Audi, Skody, Seata, Forda i marek Stellantis</strong> w oprogramowaniu producenta, online.</li>
</ul>
<h2>Sterownik kurierem</h2>
<p>Sam sterownik albo moduł możecie przysłać. Auto nie musi do nas przyjeżdżać.</p>
<ol>
<li><strong>Najpierw zadzwońcie albo napiszcie na WhatsApp.</strong> Wyślijcie zdjęcie naklejki sterownika z numerami i napiszcie, co trzeba zrobić. Potwierdzimy, czy to możliwe.</li>
<li><strong>Odłączcie akumulator przed wyjęciem sterownika.</strong></li>
<li><strong>Zapakujcie sterownik w woreczek antystatyczny</strong>, a potem w karton z wypełnieniem, żeby nie latał w środku.</li>
<li><strong>Dołóżcie kartkę</strong>: nazwa warsztatu, telefon, VIN auta, co trzeba zrobić. Przy klonowaniu wyślijcie oba sterowniki i opiszcie, który jest który.</li>
<li><strong>Odeślemy kurierem</strong> po wykonaniu usługi.</li>
</ol>
<h2>Rozliczenie</h2>
<p>Zakres i koszt ustalamy, zanim zaczniemy pracę.</p>
<p>Adres do wysyłki: AdoZ Auto, ul. Pilawska 11, 08-445 Osieck.</p>""",
 "Dla warsztatów")

# ---------- realne naprawy ----------
write("realne-naprawy.html", head("Realne naprawy — przykłady usterek elektrycznych | AdoZ Auto",
 "Opisy prawdziwych napraw z warsztatu AdoZ Auto w Osiecku: objawy, diagnoza i rozwiązanie usterek elektrycznych i elektroniki samochodowej.","realne-naprawy.html",'<meta name="robots" content="noindex">\n') + header("realne-naprawy.html") + f'''
<section class="page-hero"><div class="wrap">
<div class="crumbs"><a href="./">Strona główna</a> / Realne naprawy</div>
<h1>Realne naprawy</h1><p>Prawdziwe przypadki z naszego warsztatu: objaw, przebieg diagnozy i co okazało się przyczyną. Jeśli masz podobny problem, możliwe, że już go znamy.</p>
</div></section>
<section><div class="wrap">
<div class="empty"><h2>Pierwsze opisy napraw są w przygotowaniu</h2><p>Masz usterkę, która nie daje Ci spokoju? Opisz ją. Odpowiemy, czy możemy pomóc.</p><a class="btn btn-dark" href="kontakt.html#zgloszenie">Opisz usterkę</a></div>
</div></section>
''' + footer())

# ---------- kontakt ----------
write("kontakt.html", head("Kontakt — elektryk samochodowy Osieck | AdoZ Auto",
 "AdoZ Auto, ul. Pilawska 11, 08-445 Osieck. Tel. 511 933 675. Poniedziałek–piątek 8:00–18:00, sobota 9:00–15:00. Zgłoś usterkę online.","kontakt.html") + header("kontakt.html") + f'''
<section class="page-hero"><div class="wrap">
<div class="crumbs"><a href="./">Strona główna</a> / Kontakt</div>
<h1>Kontakt</h1><p>Najszybciej telefonicznie. Jeśli nie odbieramy, opisz usterkę w formularzu albo napisz na WhatsApp.</p>
<a class="btn btn-wire" href="tel:{TEL_H}">{ICON_PHONE}Zadzwoń: {TEL}</a>
</div></section>
<section><div class="wrap contact-grid">
<div>
<ul class="contact-list">
<li><span class="k">Telefon</span><a href="tel:{TEL_H}">{TEL}</a></li>
<li><span class="k">WhatsApp</span><a href="{WA}">Napisz wiadomość</a></li>
<li><span class="k">E-mail</span><a href="mailto:{MAIL}">{MAIL}</a></li>
<li><span class="k">Adres</span><a href="{GMAPS}" target="_blank" rel="noopener">{ADDR}</a></li>
</ul>
<table class="hours"><caption class="hp">Godziny otwarcia</caption>
<tr><td>Poniedziałek–piątek</td><td>8:00–18:00</td></tr>
<tr><td>Sobota</td><td>9:00–15:00</td></tr>
<tr><td>Niedziela</td><td>nieczynne</td></tr></table>
</div>
<iframe class="map" title="Mapa dojazdu do AdoZ Auto" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=51.9662741,21.4246991&z=16&output=embed"></iframe>
</div></section>
<section class="alt" id="zgloszenie"><div class="wrap">
<div class="section-head"><h2>Opisz usterkę</h2><p>Trzy krótkie kroki. Na końcu otworzy się SMS albo WhatsApp z gotową wiadomością do nas.</p></div>
{TICKET}
</div></section>
''' + footer())

# ---------- polityka ----------
write("polityka-prywatnosci.html", head("Polityka prywatności | AdoZ Auto","Polityka prywatności strony AdoZ Auto.","polityka-prywatnosci.html") + header("") + f'''
<section class="page-hero"><div class="wrap"><h1>Polityka prywatności</h1></div></section>
<section><div class="wrap"><div class="prose">
<h2>Administrator danych</h2>
<p>Administratorem danych osobowych jest AdoZ Auto Dawid Zadrożny, ul. Pilawska 11, 08-445 Osieck, NIP 5322117153. Kontakt: <a href="mailto:{MAIL}">{MAIL}</a>, tel. {TEL}.</p>
<h2>Jakie dane zbieramy i po co</h2>
<p>Formularze na stronie nie wysyłają danych na żaden serwer. Przygotowują tylko wiadomość, którą sam wysyłasz SMS-em albo przez WhatsApp. Dopóki jej nie wyślesz, nic do nas nie trafia.</p>
<p>Gdy piszesz, dzwonisz albo wysyłasz e-mail, dostajemy dane, które sam podajesz: imię, numer telefonu, informacje o samochodzie (marka, model, rok, VIN) oraz opis usterki. Używamy ich wyłącznie po to, żeby się z Tobą skontaktować, odpowiedzieć na zgłoszenie i umówić wizytę.</p>
<p>Podstawą przetwarzania jest podjęcie działań na Twoje żądanie przed zawarciem umowy (art. 6 ust. 1 lit. b RODO) oraz nasz prawnie uzasadniony interes, czyli obsługa zapytań (art. 6 ust. 1 lit. f RODO).</p>
<h2>Jak długo przechowujemy dane</h2>
<p>Dane ze zgłoszeń przechowujemy przez czas potrzebny do obsługi sprawy, a jeśli nie dojdzie do naprawy, nie dłużej niż 12 miesięcy. Dane związane z wykonaną usługą przechowujemy tak długo, jak wymagają tego przepisy podatkowe.</p>
<h2>Komu przekazujemy dane</h2>
<p>Dane mogą trafić do firm, które technicznie obsługują kontakt i stronę: operator sieci komórkowej (przy SMS), WhatsApp (Meta), dostawca poczty e-mail (Google) oraz GitHub, który utrzymuje stronę i zapisuje w logach technicznych adresy IP odwiedzających, żeby chronić serwis przed nadużyciami. Nie sprzedajemy danych i nie przekazujemy ich do celów marketingowych.</p>
<h2>Twoje prawa</h2>
<p>Masz prawo do dostępu do swoich danych, ich sprostowania, usunięcia, ograniczenia przetwarzania, sprzeciwu oraz przeniesienia danych. Masz też prawo złożyć skargę do Prezesa Urzędu Ochrony Danych Osobowych. Podanie danych jest dobrowolne, ale bez numeru telefonu nie będziemy mogli się z Tobą skontaktować.</p>
<h2>Pliki cookies i mapa</h2>
<p>Strona nie używa plików cookies do analityki ani reklamy. Na stronie osadzona jest mapa Google, która może zapisywać pliki cookies Google, gdy ją wyświetlasz. Zasady Google opisuje <a href="https://policies.google.com/privacy?hl=pl" rel="noopener" target="_blank">polityka prywatności Google</a>.</p>
</div></div></section>
''' + footer())

# favicon, robots, sitemap
write("favicon.svg", '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="7" fill="#14251f"/><path d="M3 18h5l2.7-8 4 16 4-12 2.7 4H29" fill="none" stroke="#4fe3b0" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/></svg>')
write("robots.txt", f"User-agent: *\nDisallow:\nSitemap: {DOMAIN}/sitemap.xml\n")
write("CNAME", "adozelektryka.pl\n")
pages = ["", "diagnostyka-komputerowa.html","elektryka-samochodowa.html","elektronika-moduly.html","klucze-samochodowe.html","sterowniki-i-moduly.html","vag-diagnostyka-i-kodowanie.html","ford-diagnostyka-i-programowanie.html","stellantis-diagnostyka-i-programowanie.html","naprawa-adblue-dpf-egr.html","chiptuning.html","dla-warsztatow.html","kontakt.html","polityka-prywatnosci.html"]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"<url><loc>{DOMAIN}/{p}</loc><lastmod>2026-11-23</lastmod></url>\n" for p in pages) + "</urlset>\n"
write("sitemap.xml", sm)
print("ok")
