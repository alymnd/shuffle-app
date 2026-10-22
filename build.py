#!/usr/bin/env python3
"""Generates the static pages of the Shuffle website (GitHub Pages). Run after editing, then commit."""
import os

SITE = "https://alymnd.github.io/shuffle-app"
CONTACT = "support@group-o-mat.de"
PROVIDER = "Alexander Münd, c/o Block Services, Stuttgarter Str. 106, 70736 Fellbach"

def page(path, lang, title, description, body, alternates):
    depth = path.count("/")
    root = "../" * depth
    nav = {
        "en": [("Home", "index.html"), ("Support", "support.html"), ("Privacy", "privacy.html"), ("Legal notice", "impressum.html")],
        "de": [("Start", "de/index.html"), ("Hilfe", "de/hilfe.html"), ("Datenschutz", "datenschutz.html"), ("Impressum", "impressum.html")],
    }[lang]
    links = "".join(f'<a href="{root}{href}">{label}</a>' for label, href in nav)
    alt = "".join(f'<link rel="alternate" hreflang="{l}" href="{SITE}/{h}">' for l, h in alternates.items())
    switch = " · ".join(
        f'<strong>{name}</strong>' if l == lang else f'<a href="{root}{alternates[l]}" hreflang="{l}">{name}</a>'
        for l, name in (("de", "Deutsch"), ("en", "English")) if l in alternates)
    html = f"""<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="stylesheet" href="{root}style.css"><link rel="icon" href="{root}favicon.png"><link rel="apple-touch-icon" href="{root}apple-touch-icon.png">
<title>{title}</title><meta name="description" content="{description}">{alt}</head><body><header><a href="{root}{nav[0][1]}"><img src="{root}icon.png" alt=""></a><strong>Shuffle</strong><nav>{links}</nav></header><main>
{body.strip()}
</main><footer><span>© 2026 Alexander Münd</span><span>{switch}</span></footer></body></html>
"""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    open(path, "w").write(html)

# ---------------------------------------------------------------- Home
page("index.html", "en", "Shuffle – Photo Slideshows for iPhone, iPad and Apple TV",
     "Play any photo album as a beautiful slideshow, shuffled or in order, with the story behind every photo.",
     """
<div class="hero"><div><h1>Your albums, beautifully replayed.</h1>
<p class="lead">Shuffle plays any album from your photo library as a slideshow – at random or in order – and tells the story behind every photo: when, where and who.</p>
<p class="avail">For iPhone and iPad with iOS 27 · Coming soon to the App Store</p></div><img src="icon.png" alt="Shuffle app icon"></div>
<div class="grid">
<div class="card"><h3>Shuffle or in order</h3><p>Random, oldest or newest first, album order, or your top-rated photos first.</p></div>
<div class="card"><h3>When, where, who</h3><p>Capture time in the local time zone, the place on a map with an exact dot, and how many people are in the picture.</p></div>
<div class="card"><h3>Apple Intelligence captions</h3><p>Short titles written on your device. Prepare an album ahead, edit captions, or save them to Photos.</p></div>
<div class="card"><h3>Made for the big screen</h3><p>Mirror to an Apple TV and Shuffle switches to a TV layout; your iPhone becomes the remote.</p></div>
<div class="card"><h3>Beautiful motion</h3><p>Ken Burns that drifts towards faces, dissolve, slide, zoom and dream transitions.</p></div>
<div class="card"><h3>Only the photos you want</h3><p>Screenshots, receipts and near-identical shots are left out. Rate, favorite or hide a photo while it plays.</p></div>
<div class="card"><h3>Music and weather</h3><p>A playlist, album or song from Apple Music plays along, and a small icon shows the current weather.</p></div>
<div class="card"><h3>Picture frame</h3><p>An album shuffles full screen with a clock, goes dark at night and stays on while charging.</p></div>
<div class="card"><h3>Private by design</h3><p>No account, no tracking, no ads. Your photos never leave your device.</p></div>
</div>
<p>Questions? See <a href="support.html">Support</a>.</p>
""", {"en": "index.html", "de": "de/index.html"})

page("de/index.html", "de", "Shuffle – Foto-Diashows für iPhone, iPad und Apple TV",
     "Spiele jedes Fotoalbum als schöne Diashow ab, zufällig oder der Reihe nach, mit der Geschichte hinter jedem Foto.",
     """
<div class="hero"><div><h1>Deine Alben, schön in Szene gesetzt.</h1>
<p class="lead">Shuffle spielt jedes Album deiner Fotomediathek als Diashow ab – zufällig oder der Reihe nach – und erzählt die Geschichte hinter jedem Foto: wann, wo und wer.</p>
<p class="avail">Für iPhone und iPad ab iOS 27 · Bald im App Store</p></div><img src="../icon.png" alt="App-Symbol von Shuffle"></div>
<div class="grid">
<div class="card"><h3>Zufällig oder der Reihe nach</h3><p>Zufällig, älteste oder neueste zuerst, Album-Reihenfolge oder die am besten bewerteten Fotos zuerst.</p></div>
<div class="card"><h3>Wann, wo, wer</h3><p>Aufnahmezeit in der Ortszeit, der Ort auf einer Karte mit genauem Punkt und wie viele Personen zu sehen sind.</p></div>
<div class="card"><h3>Bildunterschriften mit Apple Intelligence</h3><p>Kurze Titel, auf deinem Gerät geschrieben. Bereite ein Album vor, bearbeite Bildunterschriften oder sichere sie in Fotos.</p></div>
<div class="card"><h3>Für den großen Bildschirm</h3><p>Spiegle auf ein Apple TV und Shuffle wechselt in eine TV-Ansicht; dein iPhone wird zur Fernbedienung.</p></div>
<div class="card"><h3>Schöne Bewegung</h3><p>Ken-Burns-Effekt, der zu Gesichtern wandert, Überblenden, Schieben, Zoomen und Traum-Übergänge.</p></div>
<div class="card"><h3>Nur die Fotos, die du sehen willst</h3><p>Bildschirmfotos, Belege und fast gleiche Aufnahmen bleiben draußen. Bewerte, markiere oder blende Fotos während der Wiedergabe aus.</p></div>
<div class="card"><h3>Musik und Wetter</h3><p>Eine Playlist, ein Album oder ein Titel aus Apple Music läuft mit, und ein kleines Symbol zeigt das aktuelle Wetter.</p></div>
<div class="card"><h3>Bilderrahmen</h3><p>Ein Album läuft zufällig im Vollbild mit Uhr, wird nachts dunkel und bleibt beim Laden an.</p></div>
<div class="card"><h3>Privat von Grund auf</h3><p>Kein Konto, kein Tracking, keine Werbung. Deine Fotos verlassen dein Gerät nie.</p></div>
</div>
<p>Fragen? Siehe <a href="hilfe.html">Hilfe</a>.</p>
""", {"en": "index.html", "de": "de/index.html"})

# ---------------------------------------------------------------- Support
page("support.html", "en", "Support – Shuffle", "Help and contact for the Shuffle app.", f"""
<h1>Support</h1>
<p>Write to <a href="mailto:{CONTACT}?subject=Shuffle">{CONTACT}</a> (subject “Shuffle”). Please include your device and iOS version.</p>
<h2>Getting started</h2>
<p>Allow access to your photos, pick an album and tap <strong>Play</strong> or <strong>Shuffle</strong>. Tap a photo in the album to start from there. During the slideshow, tap to show the controls, swipe left or right to skip, swipe down to close, and tap the details card for everything about a photo.</p>
<h2>Apple TV</h2>
<p>Open Control Center, tap Screen Mirroring and choose your Apple TV. Shuffle shows a layout made for the TV and your iPhone becomes the remote. Turn off “TV Layout” in Settings to mirror the phone instead.</p>
<h2>Captions</h2>
<p>Captions are written by Apple Intelligence on your device and need a device that supports it, with Apple Intelligence turned on. On an album page, “Prepare” writes captions for every photo ahead of time. Keep Shuffle open while it works (the screen stays on); if you leave the app it pauses and continues when you come back. You can edit, regenerate or remove a caption in a photo's details.</p>
<h2>Why aren't people named?</h2>
<p>iOS doesn't give apps the names from the People album in Photos. Shuffle detects faces on your device to count people and to focus the Ken Burns effect, but it can't tell who they are.</p>
<h2>I only see some of my photos</h2>
<p>You may have granted limited access. Change it in Settings → Apps → Shuffle → Photos → Full Access.</p>
<p>Also see the <a href="privacy.html">privacy policy</a>.</p>
""", {"en": "support.html", "de": "de/hilfe.html"})

page("de/hilfe.html", "de", "Hilfe – Shuffle", "Hilfe und Kontakt zur App Shuffle.", f"""
<h1>Hilfe</h1>
<p>Schreib an <a href="mailto:{CONTACT}?subject=Shuffle">{CONTACT}</a> (Betreff „Shuffle“). Nenne bitte dein Gerät und deine iOS-Version.</p>
<h2>Erste Schritte</h2>
<p>Erlaube den Zugriff auf deine Fotos, wähle ein Album und tippe auf <strong>Abspielen</strong> oder <strong>Zufällig</strong>. Tippe auf ein Foto im Album, um dort zu beginnen. In der Diashow blendet ein Tipp die Steuerung ein, Wischen nach links oder rechts blättert, Wischen nach unten schließt, und die Detailkarte zeigt alles zum Foto.</p>
<h2>Apple TV</h2>
<p>Öffne das Kontrollzentrum, tippe auf „Bildschirmsynchronisierung“ und wähle dein Apple TV. Shuffle zeigt eine eigene TV-Ansicht, und dein iPhone wird zur Fernbedienung. Schalte „TV-Ansicht“ in den Einstellungen aus, um stattdessen das iPhone zu spiegeln.</p>
<h2>Bildunterschriften</h2>
<p>Bildunterschriften schreibt Apple Intelligence auf deinem Gerät; dafür braucht es ein unterstütztes Gerät mit eingeschalteter Apple Intelligence. Auf der Seite eines Albums schreibt „Vorbereiten“ die Bildunterschriften für alle Fotos im Voraus. Lass Shuffle dabei geöffnet (der Bildschirm bleibt an); verlässt du die App, pausiert es und geht weiter, sobald du zurückkommst. In den Details eines Fotos kannst du eine Bildunterschrift bearbeiten, neu erstellen oder entfernen.</p>
<h2>Warum werden Personen nicht mit Namen genannt?</h2>
<p>iOS gibt die Namen aus dem Album „Personen“ der Fotos-App nicht an andere Apps weiter. Shuffle erkennt Gesichter auf deinem Gerät, um Personen zu zählen und den Ken-Burns-Effekt auszurichten, weiß aber nicht, wer sie sind.</p>
<h2>Ich sehe nur einige Fotos</h2>
<p>Vermutlich hast du nur eingeschränkten Zugriff erlaubt. Ändere das unter Einstellungen → Apps → Shuffle → Fotos → Voller Zugriff.</p>
<p>Siehe auch die <a href="../datenschutz.html">Datenschutzerklärung</a>.</p>
""", {"en": "support.html", "de": "de/hilfe.html"})

# ---------------------------------------------------------------- Privacy
page("datenschutz.html", "de", "Datenschutzerklärung – Shuffle", "Datenschutzerklärung der App Shuffle und dieser Website.", f"""
<h1>Datenschutzerklärung für Shuffle</h1>
<p>Stand: 22. Oktober 2026 (Fotoauswahl und ausgeblendete Fotos ergänzt). Diese deutsche Fassung ist maßgeblich.</p>
<p><strong>Verantwortlicher:</strong> {PROVIDER}, Deutschland; E-Mail <a href="mailto:{CONTACT}">{CONTACT}</a></p>
<p><strong>Kurz gesagt:</strong> Shuffle hat keinen eigenen Server, keine Konten, keine Werbung und kein Tracking und enthält keine Analyse-, Werbe- oder Absturzberichts-Bibliotheken von Drittanbietern. Der Entwickler erhält keine deiner Daten.</p>
<p><strong>Fotomediathek:</strong> Mit deiner Erlaubnis liest die App Fotos, Alben und deren Metadaten (Aufnahmezeit, Ort, Kameradaten, Favoriten, Bewertungen, Bildunterschriften, Schlagwörter), um sie anzuzeigen. Sie schreibt nur, wenn du es auslöst: Favorit setzen, Bewertung ändern (auch während der Diashow) oder eine Bildunterschrift „Auch in Fotos sichern“. iOS fragt dabei jedes Mal nach.</p>
<p><strong>Verarbeitung auf dem Gerät:</strong> Gesichts- und Personenerkennung (Apple Vision) zählt Personen und richtet den Bildausschnitt aus; es findet keine Identifizierung statt, und die Ergebnisse werden nicht gespeichert. Bildunterschriften erstellt Apple Intelligence (Foundation-Models-Framework) vollständig auf dem Gerät; sie werden im geschützten Container der App gespeichert, bis du sie in den Einstellungen löschst oder die App entfernst. Die Fotoauswahl (Apple Vision) erkennt auf dem Gerät Bildschirmfotos, Fotos von Belegen und Dokumenten sowie fast gleiche Aufnahmen.</p>
<p><strong>Ausgeblendete und übersprungene Fotos:</strong> Blendest du ein Foto aus, merkt sich die App seine Kennung in einer Liste im geschützten Container auf dem Gerät, ebenso die erkannten Bildschirmfotos und Dokumente. Die Fotos selbst bleiben unverändert in deiner Mediathek. Unter Einstellungen → Fotoauswahl → Übersprungene Fotos holst du ausgeblendete Fotos zurück; das Entfernen der App löscht die Liste.</p>
<p><strong>Karten und Orte:</strong> Hat ein Foto einen Aufnahmeort, sendet die App dessen Koordinaten an Apple Maps (MapKit), um den Ortsnamen zu ermitteln und die Karte zu zeigen. Dafür gilt die Datenschutzrichtlinie von Apple. An den Entwickler wird nichts übermittelt.</p>
<p><strong>Apple TV und Siri:</strong> Bei der Bildschirmsynchronisierung zeigt die App Fotos über AirPlay auf deinem Fernseher. Für Siri und Kurzbefehle stellt die App Albennamen dem System zur Verfügung.</p>
<p><strong>Musik:</strong> Wählst du Musik aus Apple Music, fragt die App mit deiner Erlaubnis über Apples MusicKit deine Mediathek ab, durchsucht den Apple-Music-Katalog und spielt die Musik ab; dafür gilt die Datenschutzrichtlinie von Apple. Gespeichert wird nur deine Auswahl, lokal auf dem Gerät; an den Entwickler wird nichts übermittelt.</p>
<p><strong>Wetter:</strong> Ist „Aktuelles Wetter“ eingeschaltet, fragt die App mit deiner Erlaubnis deinen ungefähren Standort ab (keine genaue Position) und sendet ihn an Apple Wetter (WeatherKit), um das aktuelle Wetter anzuzeigen; dafür gilt die Datenschutzrichtlinie von Apple. Es wird nur der ungefähre Standort verwendet und nur für diese Anfrage an Apple Wetter; er wird nicht gespeichert und nicht an den Entwickler übermittelt.</p>
<p><strong>Einstellungen:</strong> Deine Einstellungen speichert die App lokal auf dem Gerät.</p>
<p><strong>Löschen:</strong> „Alle Bildunterschriften löschen“ in den Einstellungen entfernt die gespeicherten Bildunterschriften, „Übersprungene Fotos“ holt ausgeblendete Fotos zurück; das Entfernen der App löscht alle lokalen Daten. In Fotos gesicherte Bildunterschriften, Favoriten und Bewertungen bleiben in deiner Fotomediathek.</p>
<p><strong>Deine Rechte:</strong> Da der Entwickler keine personenbezogenen Daten erhält, erfolgen Auskunft, Berichtigung und Löschung direkt in der App. Bei Fragen wende dich an den Verantwortlichen; du kannst dich bei einer Datenschutz-Aufsichtsbehörde beschweren.</p>
<h2>Diese Website</h2><p>Diese Website ist eine statische Seite ohne Cookies, Analyse oder eingebettete Inhalte Dritter. Sie wird von GitHub Pages (GitHub, Inc., USA) ausgeliefert, das deine IP-Adresse technisch bedingt in Server-Logs verarbeitet (<a href="https://docs.github.com/de/site-policy/privacy-policies/github-general-privacy-statement">Datenschutzerklärung von GitHub</a>). Schreibst du uns eine E-Mail, nutzen wir Adresse und Nachricht nur zur Antwort.</p>
""", {"de": "datenschutz.html", "en": "privacy.html"})

page("privacy.html", "en", "Privacy Policy – Shuffle", "Privacy policy of the Shuffle app and this website.", f"""
<h1>Privacy Policy for Shuffle</h1>
<p>Last updated: 22 October 2026 (photo selection and hidden photos added). This is a courtesy translation; the German version is authoritative.</p>
<p><strong>Controller:</strong> {PROVIDER}, Germany; e-mail <a href="mailto:{CONTACT}">{CONTACT}</a></p>
<p><strong>In short:</strong> Shuffle has no server of its own, no accounts, no ads and no tracking, and contains no third-party analytics, advertising or crash-reporting libraries. The developer never receives any of your data.</p>
<p><strong>Photo library:</strong> with your permission the app reads photos, albums and their metadata (capture time, location, camera details, favourites, ratings, captions, keywords) to display them. It only writes when you trigger it: marking a favourite, changing a rating (also during a slideshow), or “Also Save to Photos” for a caption. iOS asks for confirmation each time.</p>
<p><strong>On-device processing:</strong> face and person detection (Apple Vision) counts people and frames the picture; nobody is identified and the results are not stored. Captions are written by Apple Intelligence (Foundation Models framework) entirely on the device; they are stored in the app's protected container until you delete them in Settings or remove the app. Photo selection (Apple Vision) recognises screenshots, photos of receipts and documents, and almost identical shots on the device.</p>
<p><strong>Hidden and skipped photos:</strong> when you hide a photo, the app keeps its identifier in a list in its protected container on the device, together with the screenshots and documents it detected. The photos themselves stay unchanged in your library. Restore hidden photos in Settings → Photo Selection → Hidden Photos; removing the app deletes the list.</p>
<p><strong>Maps and places:</strong> if a photo has a location, the app sends its coordinates to Apple Maps (MapKit) to look up the place name and show the map. Apple's privacy policy applies. Nothing is sent to the developer.</p>
<p><strong>Apple TV and Siri:</strong> during Screen Mirroring the app shows photos on your TV via AirPlay. For Siri and Shortcuts the app provides album names to the system.</p>
<p><strong>Music:</strong> if you choose music from Apple Music, the app uses Apple's MusicKit with your permission to read your library, search the Apple Music catalog and play the music; Apple's privacy policy applies. Only your choice is stored, locally on the device; nothing is sent to the developer.</p>
<p><strong>Weather:</strong> if "Current Weather" is on, the app asks for your approximate location (not your precise position) with your permission and sends it to Apple Weather (WeatherKit) to show the current weather; Apple's privacy policy applies. Only the approximate location is used, and only for this request to Apple Weather; it is neither stored nor sent to the developer.</p>
<p><strong>Settings:</strong> your settings are stored locally on the device.</p>
<p><strong>Deletion:</strong> “Delete All Captions” in Settings removes stored captions, and “Hidden Photos” brings hidden photos back; removing the app deletes all local data. Captions saved to Photos, favourites and ratings stay in your photo library.</p>
<p><strong>Your rights:</strong> since the developer receives no personal data, access, rectification and erasure happen directly in the app. Contact the controller above with questions; you may lodge a complaint with a supervisory authority.</p>
<h2>This website</h2><p>This is a static site without cookies, analytics or embedded third-party content. It is served by GitHub Pages (GitHub, Inc., USA), which processes your IP address in server logs as technically required (<a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">GitHub privacy statement</a>). If you e-mail us, we use your address and message only to reply.</p>
""", {"de": "datenschutz.html", "en": "privacy.html"})

# ---------------------------------------------------------------- Imprint
page("impressum.html", "de", "Impressum – Shuffle", "Impressum der Website zur App Shuffle.", f"""
<h1>Impressum</h1>
<p><strong>Angaben gemäß § 5 DDG</strong><br>Alexander Münd<br>c/o Block Services<br>Stuttgarter Str. 106<br>70736 Fellbach<br>Deutschland</p>
<p>E-Mail: <a href="mailto:{CONTACT}">{CONTACT}</a></p>
<p>Verantwortlich für den Inhalt: Alexander Münd, Anschrift wie oben.</p>
<h2>Legal notice (English)</h2>
<p>Information according to § 5 DDG (German Digital Services Act). Provider and person responsible for content: {PROVIDER}, Germany, e-mail <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>
<h2>Marken</h2><p>Apple, iPhone, iPad, Apple TV, AirPlay, Apple Intelligence und App Store sind Marken von Apple Inc.</p>
""", {"de": "impressum.html", "en": "impressum.html"})

print("pages written")
