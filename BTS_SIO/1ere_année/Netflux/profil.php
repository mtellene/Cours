<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
        <title>Accueil - Netflux</title>
        <link rel="stylesheet" href="style.css">
        <link rel="stylesheet" media="screen and (max-width: 1000px)" href="style_telephone.css">
    </head>

    <body>
        <header>
            <nav>
                <ul>
                    <li>Accueil</li>
                    <li>Séries</li>
                    <li>Films</li>
                    <li>Nouveautés les plus regardées</li>
                    <li>Ma liste</li>
                    <li>Explorer par langue</li>
                </ul>
            </nav>
        </header>

        <div id="tendances_actuelles">
            <h2>Tendances actuelles</h2>

            <div id="series">
                <button id="pred">&#12296;</button>

                <ul>
                    <li id="li_item1">
                        <img src="images/tendances/tendance1.jpg" id="item1" alt="item1">
                        <span id="span_item1" class="serie"></span>
                    </li>

                    <li id="li_item2">
                        <img src="images/tendances/tendance2.jpg" id="item2" alt="item2">
                        <span id="span_item2" class="serie"></span>
                    </li>
                    <li id="li_item3">
                        <img src="images/tendances/tendance3.webp" id="item3" alt="item3">
                        <span id="span_item3" class="serie"></span>
                    </li>
                    <li id="li_item4">
                        <img src="images/tendances/tendance4.webp" id="item4" alt="item4">
                        <span id="span_item4" class="serie"></span>
                    </li>
                    <li id="li_item5">
                        <img src="images/tendances/tendance5.jpg" id="item5" alt="item15">
                        <span id="span_item5" class="serie"></span>
                    </li>
                </ul>

                <button id="suiv">&#12297;</button>
            </div>
        </div>
    </body>
</html>
