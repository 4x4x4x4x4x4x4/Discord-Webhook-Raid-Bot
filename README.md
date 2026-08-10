⚙️ Jak to funguje v praxi

Tyhle boty fungují na jednoduchém principu – opakovaně posílají požadavky na Discord API. Když k tomu přidáte webhook, může to vypadat třeba takhle:

    Získání a konfigurace webhooku – Webhook je v podstatě speciální URL adresa, která propojuje Discord s ostatními aplikacemi. Spammer si buď vytvoří vlastní webhook v kanálu, nebo použije už existující .

    Samotný spam – Bot potom v nekonečné smyčce posílá HTTP POST požadavky na URL toho webhooku. Každý požadavek obsahuje zprávu, kterou chce odeslat .

    Hromadný spam – Aby byl spam ještě intenzivnější, některé nástroje umí posílat zprávy paralelně pomocí vláken (threads), čímž dokážou zahltit kanál během pár vteřin .

🧰 Co na GitHubu najdete

Prohledáte-li GitHub, narazíte na celou řadu takových repozitářů. Často mají velmi podobnou strukturu:

    Hlavní funkce: Kromě spamování webhooků umí obvykle i mazat kanály, role, banovat uživatele nebo vytvářet stovky nových kanálů najednou .

    Jazyk: Většina je psaná v Pythonu (knihovny discord.py, requests) nebo v JavaScriptu/TypeScriptu (knihovna discord.js) .

    Jednoduché nastavení: Stačí nakonfigurovat token bota, nastavit prefix pro příkazy a bot je připravený k použití .

Dobrým příkladem, jak tahle "výuka" vypadá, je projekt raidbotdiscord. V jeho README.md najdete příkazy jako .des pro zničení serveru, .del pro smazání kanálů nebo .r pro získání admin role. K tomu samozřejmě nechybí ani sekce s instalací a konfigurací .
⚠️ Problém a jeho důsledky

I když se tyto projekty tváří nevinně, problém je jasný – při nesprávném použití snadno porušují Discord Terms of Service. Důsledky mohou být vážné.

Dobře to ilustruje i bezpečnostní chyba (CVE-2026-41899) v aplikaci Coolify, kde neautentizovaný endpoint bez omezení posílal uživatelský vstup přímo na Discord webhook. Tohle není ani tak o botovi, jako o tom, k čemu může vést nezabezpečený webhook :

    Spam a DoS (Denial of Service): Stačí jednoduchý skript na posílání požadavků a Discord webhook se dá snadno zahltit. Tím se zablokují legitimní notifikace a kanál se stane nepoužitelným .

    Phishing a podvody: Útočník může posílat zprávy, které vypadají jako oficiální oznámení, a šířit tak odkazy na phishingové stránky. Vzhledem k tomu, že zpráva jde skrz webhook, vypadá důvěryhodně .

    Poškození reputace: Skrz webhook lze posílat spam nebo urážlivý obsah, čímž se poškodí jméno majitele serveru nebo dané aplikace .

🌐 Širší kontext a alternativa

Zajímavé je, že na GitHubu najdete i projekty s opačným cílem – anti-raid boty, které mají chránit servery právě před podobnými útoky. Ty hlídají nové členy, automaticky je vykopávají nebo zapínají pomalý režim . Je to další ukázka, že jde o velmi citlivé a často zneužívané téma.

Stručně řečeno, raideři na Discordu jsou často jednoduché skripty, které zneužívají sílu botů a webhooků. GitHub je plný jejich zdrojových kódů, ale jejich použití je v rozporu s pravidly Discordu a může vést k zablokování účtu. Vždy je lepší držet se oficiálních a povolených způsobů, jak s Discord boty pracovat.
