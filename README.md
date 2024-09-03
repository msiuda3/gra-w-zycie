# gra-w-zycie
Prosty program napisany w python symulujący działanie aparatu komórkowego wymyślony przez Johna Conwaya.
https://pl.wikipedia.org/wiki/Gra_w_%C5%BCycie

# Uruchomienie
Program korzysta z modułu pygame do wyświetlania interfejsu użytkownika. Do uruchomienia programu wymagane jest zainstalowanie tego pakietu.
W celu uruchomienia programu należy uruchomić skrypt main.py ('python3 main.py')
	
# Korzystanie z programu:
Po uruchomieniu programu wyświetlona zostaje siatka 20x20 reprezentująca poszczególne komórki modelu. Czerwony kolor oznacza, że dana komórka jest martwa. Zielony oznacza komórkę żywą.
W dowolnym momencie użytkownik może zmienić stan dowolnej komórki klikając na nią kursorem lewym przyciskiem myszy.
Kliknięcie przycisku "Następny cykl", bądź naciśnięcie klawiszu spacji spowoduje przejście do następnego cyklu i zaktualizowanie stanu wszystkich komórek zgodnie z zasadami "gry w życie".

# Dodatkowe informacje:
Do projektu załączane są dwa screny.
"start.png" pokazuje przykładowy początkowy stan ustawiony przez użytkownika. "kolejny_cykl.png" pokazuje efekt po jednorazowym przejściu cyklu tego ustawienia.
