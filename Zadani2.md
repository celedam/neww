## Guideline pro výuku Python Django

Zde je komplexní plán pro výuku Python Django, rozdělený do klíčových okruhů. Po každém okruhu následují otázky, které pomohou ověřit pochopení daného tématu.

### 1. Základy Pythonu

Před začátkem práce s Djangem je nezbytné mít solidní znalosti Pythonu[3].

**Otázky:**
- Vysvětlete rozdíl mezi listem a tuple v Pythonu.
  LIST - může se měnit, zapisuje se s hranatými závorkami, je pomalejší, je vhodný pro situace kde chceme měnit obsah listu
  TUPLE - nemůže se měnit, zapisuje se s kulatými závorkami, je rychlejší protože python nečeká na změny s tuplem, využívá se v situacích kdy víme že se obsah nebude měnit
  
- Jak fungují dekorátory v Pythonu a k čemu se používají?
  je to funkce která příjmá jinou funkci jako parametr, da se říct že vylepšuje původní funkci, používáme ji na zaznamenávání logů, autorizaci, měření výkonosti, úprava chování funkcí bez změny zdrojového kódu atd.
  
- Napište příklad použití list comprehension.
names = ["alice", "bob", "charlie", "diana"]
uppercase_names = [name.upper() for name in names]
print(uppercase_names)

je to práce s listem za pomocí jenom jednoho řádku


### 2. Úvod do Django

Seznámení s Django frameworkem, jeho architekturou a základními koncepty[1][4].

**Otázky:**
- Co je to MVT architektura a jak se liší od MVC?
  MVT = model-view-template, model - drží logiku a data aplikace/webovky, view - je zodpovědné za GUI, template - vkládá data do HTML **používá se v Djangu**
  MVC = model-view-controller, model - stejný jak v MVT, view - stejný jak v MVT, controller - hlídá co uživatel dělá a co se má zobrazit **používá se v ruby on rails, angular**
  
- Vysvětlete, co je to Django projekt a co je Django aplikace.
  PROJKET obsahuje nastavení a všechný potřebné soubory k aplikaci
  APLIKACE je menší, samostatná část projektu která realizuje určitou činnost
  
- Jak vytvoříte nový Django projekt pomocí příkazové řádky?
  1. musíme mít nainstalovaný Django
  2. vytvoříme projekt, je to složka která obsahuje výchozí strukturu projektu: django-admin startproject myproject
  3. pro ověření správnosti vytvoření projektu spustíme vývojový server který se nachazí ve složce myproject, zadáme tento kód: python manage.py runserver pokud vše proběhlo správně měli by jsme vidět něco takového: Starting development server at http://127.0.0.1:8000/ Quit the server with CONTROL-C. když klikneš       na http... tak se otevře prohlížeč na stránce djanga který potrvzuje že server běží 

### 3. URL Routing a Views

Pochopení, jak Django zpracovává požadavky a směruje je na příslušné views[4].

**Otázky:**
- Jak definujete URL patterns v Django?
  definují se v urls.py, který je součástí každého projektu a každé aplikace
    aplikace - každá aplikace může mít své urls.py které definují URL patterns pro konkrétní aplikaci, tento soubor obsahuje seznam URL cest které vedou na různé view
    projekt - tento urls.py obsahuje URL na všechny aplikace aby vše bylo propojené
  použití **name** - přidává jméno každé URL
  
- Vysvětlete rozdíl mezi function-based views a class-based views.
  FBV - jsou jednoduché funkce které příjmají request jako argument a vracejí response
      výhody - jednoduchost; plná kontrola nad tím, jak požadavky zpracováváš a jeké akce vykonáváš; můžeš použít libovolnou logiku pro rozhodování o tom, jak se má response sestavit.
      nevýhody - pokud je více podobných views, může dojít k opakování kódu; čím víc je složitější aplikace, tím víc je obtížnější spravovat větší počet funkcí, protože každý nový view přidává novou funkci

  CBV - je to zaležené na třídách které poskytují přehlednější a organizovanější způsob  jak zpracovávat požadavky, místo psaní jedné funkce, která dělá vše, rozdělujeme logiku do tříd
      výhody - znovu použitelný kód; umožňuje rozdělit logiku do menších celků
      nevýhody - složitější na pochopení, protože se pracuje s třídami a objekty; není tak jasně přehledný
  
- Jak předáváte parametry z URL do view funkce?
  děláme to prostřednictvím URL patterns, kde za pomoci dynamicke URL zachytíme parametr který chceme předat, ten pak předáme jako parametr
  
### 4. Models a ORM

Práce s databází pomocí Django ORM[3][5].

**Otázky:**
- Jak definujete model v Django?
  model definujeme pomocí třídy která dědí django.db.models.Models (from django.db import models), tato třída definuje tabulku která pracuje s daty
  
- Vysvětlete, co jsou to migrace a jak je vytvoříte a aplikujete.
  je to mechanismus pro změny v datech 
  
- Napište příklad QuerySetu pro filtrování a řazení dat.

  # Získání knih, které napsal konkrétní autor
  books_by_author = Book.objects.filter(author="J.K. Rowling")

  # Získání knih, které byly vydány po roce 2000
  books_after_2000 = Book.objects.filter(published_date__year__gt=2000)

  # Získání knih, které mají "Harry" v názvu
  books_with_title = Book.objects.filter(title__icontains="Harry")


### 5. Templates

Tvorba dynamických HTML stránek pomocí Django template language[4].

**Otázky:**
- Jak v šabloně zobrazíte data předaná z view?
  data předáváme pomocí contextu (dictionary který obsahuje všechny proměnné které chceme předat), django také umožňuje pracovat s filtry přímo v šablonách
  
- Vysvětlete, jak funguje dědičnost šablon v Django.
  šablony dědíme pomocí tagů {% block %} - blok definuje místa v podřízené šabloně které jdou přepsat, každý blok má svůj název; a {% extends %} - používá se na začátku podřízené šablony a odkazuje na základní šablonu která se bude dědit
  
- Jak vytvoříte vlastní template tag?
  vytvořením vlastího tagu umožňuje přídat do šablon vlastní logiku,
  1. vytvoření složky pro custom template tagy
  2. definice vlastního teplate tagu (custom_tags.py)
  3. načtení tagů do šablony
     

### 6. Forms

Zpracování uživatelských vstupů pomocí Django forms[4].
**form jsou formulare**

**Otázky:**
- Jaký je rozdíl mezi ModelForm a Form?
  **form** je formular ktery neni propojeny s databazemi, vsechny pole formuláře musíš definovat ručně
  **modelform** je primo napojeny na datovou tabulku (model), django automaticky generuje pole formulare na základě polí v tabulce
  
- Jak validujete data v Django formuláři?
  v djangu validujeme (kontrolujeme) pomoci validace na úrovni pole nebo celého formuláře
  pole - kontrolujeme kazdé pole samostatně
  formulář - zde si můžeš nastavit vlastní logiku pro kontrolu polí v celém formuláři
   
- Jak zpracujete nahrávaní souborů pomocí formuláře?
  k zpracovaní souborů pomocí formulářů používáme FileField nebo ImageField a musíme správně nastavit view pro zpracování souborů

### 7. Authentication a Authorization

Implementace uživatelských účtů a oprávnění[5].

**Otázky:**
- Jak implementujete přihlášení a odhlášení uživatele v Django?
- Vysvětlete rozdíl mezi authentication a authorization.
- Jak omezíte přístup k view pouze pro přihlášené uživatele?

### 8. Admin rozhraní

Využití a přizpůsobení Django admin rozhraní[5].

**Otázky:**
- Jak zaregistrujete model do admin rozhraní?
  1. vytvoření modelu
  2. vytvoření administrátorského zápisu pro model
  3. pokročilé přizpůsobení admin rozhraní
     
- Jak přizpůsobíte zobrazení modelu v admin rozhraní?
  list_display: Určuje, které sloupce se zobrazí v seznamu objektů modelu.
  search_fields: Určuje, podle jakých polí lze provádět vyhledávání.
  list_filter: Umožňuje filtrovat objekty podle specifikovaných polí.
  ordering: Určuje, podle kterého pole budou objekty seřazeny.
  list_editable: Umožňuje úpravu polí přímo v seznamu.
  fields: Určuje, jaká pole se zobrazí na detailní stránce objektu.
  readonly_fields: Určuje, která pole budou pouze pro čtení.
  
- Vysvětlete, co jsou to admin actions a jak je vytvoříte.
  admin actions jsou akce které admini můžou provádět hromadně na více oběktech,
  vytvoříme je:
  1. definicí akce - je to funkce která příjmá parametry **requst** a **queryset(objekty)** a provádí nějakou změnu na techto objektech
  2. registrace akce - Akce jsou registrovány pomocí atributu actions v administrátorské třídě, který obsahuje seznam metod (funkcí) definovaných v této třídě

### 9. REST API s Django REST framework

Tvorba API endpointů pomocí Django REST framework[7].

**Otázky:**
- Co je to serializer a k čemu slouží?
  serializer je nástroj v pythonu který převádí data z pythonu aby šli jednoduše posílat přes API
  
- Jak implementujete CRUD operace pomocí ViewSets?
  pro to se používají viewsets, což jsou třídy které poskytují automatické implementace zlákladnch operací na datech, dělají automatickou logiku takže ji nemusíme psát ručně
  
- Vysvětlete, jak funguje autentizace v Django REST framework.
    1. autorizační třída (určuje jak bude uživatel ověřen)
    2. oprávnění (urcuje zda uzivatel má oprávnění k určitému zdroji)
    3. autentizační systém

       pro autentizaci používáme několik metod:
       1. basic authentication (uzivatel musí poslat své přihlašovací údaje)
       2. token autgentication (po přihlášení uživatel dostane token který je šifrovaný a používá se ke všem dalším ověřovaní)
       3. session authentication (používá cookies)


### 10. Testování

Psaní a spouštění testů pro Django aplikace[5].

**Otázky:**
- Jaké typy testů můžete psát v Django?
- Jak vytvoříte test case pro testování view?
- Vysvětlete, co je to test fixture a jak ji použijete.

### 11. Deployment

Nasazení Django aplikace do produkčního prostředí[5].

**Otázky:**
- Jaké kroky jsou nezbytné pro nasazení Django aplikace?
- Vysvětlete, proč je důležité používat HTTPS v produkci.
- Jak nakonfigurujete Django pro použití s Gunicorn a Nginx?

### 12. Pokročilé koncepty

Hlubší porozumění pokročilým funkcím Django[5].

**Otázky:**
- Vysvětlete, jak fungují middleware v Django a k čemu se používají.
- Jak implementujete full-text vyhledávání v Django?
- Vysvětlete koncept signálů v Django a uveďte příklad jejich použití.

Tímto guideline a sadou otázek můžete komplexně otestovat znalosti studenta v oblasti Python Django. Pokud student dokáže odpovědět na většinu těchto otázek a aplikovat znalosti v praxi, lze předpokládat, že má solidní porozumění Django frameworku a je schopen vyvíjet robustní webové aplikace[6][8].

Citations:
[1] https://www.w3schools.com/django/
[2] https://codewithmosh.com/p/the-ultimate-django-series
[3] https://www.linkedin.com/pulse/step-by-step-python-django-roadmap-one-year-along-naem-azam-chowdhury
[4] https://dev.to/maxrpark/python-django-the-practical-guide-2kpk
[5] https://github.com/faresemad/Django-Roadmap
[6] https://www.geeksforgeeks.org/django-tutorial/
[7] https://tech.raturi.in/django-roadmap/
[8] https://blog.jetbrains.com/pycharm/2024/01/how-to-learn-django/
[9] https://www.wscubetech.com/resources/django/free-course
[10] https://www.youtube.com/watch?v=HqsOoP2_3_0
[11] https://www.youtube.com/watch?v=Rp5vd34d-z4
[12] https://www.nobledesktop.com/outlines/python-web-development-with-django-syllabus.pdf
[13] https://www.nobledesktop.com/learn/django/prerequisites
[14] https://forum.djangoproject.com/t/learning-django-road-map/3689
