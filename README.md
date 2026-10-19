# Python Password Checker

Det här är första gången jag sätter mig ner och försöker koda något helt själv från början till slut, som en del av min utbildning till IT-säkerhetsspecialist. Det blev minst sagt några stunder där det kändes som att man blev helt varm om huvudet, men det var otroligt roligt när bitarna föll på plats!

## Bakgrund & Hur projektet växte
Jag ville lära mig Python hands-on. Det började med en första version (`password_v1.py`), men jag tyckte inte att den var särskilt smidig eftersom man fastnade vid varje enskilt steg tills man uppfyllde just det kravet. 

Därför gjorde jag om strukturen i `password_checker.py` så att den kontrollerar alla kriterier samtidigt och listar allt som saknas på en gång. När det väl flöt på var det så kul att jag ville bygga vidare och lägga till en extra säkerhet med lösenordsbekräftelse (*Confirm password*) och stjärnor i terminalen.

## Vad programmet gör
- Kollar att lösenordet är minst 12 tecken.
- Ser till att det finns minst en stor bokstav, en siffra och ett specialtecken (!@#\$%^&*).
- Döljer lösenordet när man skriver och visar stjärnor (*) istället (använder `msvcrt` för Windows).
- Skriver ut alla fel samtidigt om man missar något, så man slipper gissa sig fram en sak i taget.
- Ber en att bekräfta lösenordet en extra gång så man inte stavar fel.
- Man kan trycka Ctrl + C för att avbryta och stänga av när man vill.

## Credits & Funktioner jag har lånat
Hjälpfunktionen för att få fram stjärnor (*) i realtid i terminalen med msvcrt är en bit kod jag har lånat/fått hjälp med att integrera, eftersom det var på en ganska avancerad nivå för ett förstaprojekt. All annan valideringslogik, loopar och struktur har jag skrivit och kämpat mig igenom själv!

## Hur man kör det
Koden är gjord för Windows (eftersom den använder `msvcrt`):
```bash
python password_checker.py