<?php
    session_start();
    require '../db.php';

    if (!isset($_SESSION['user'])){
        header("Location: index.php");
        exit();
    }

    $user = $_SESSION['user'];

$sql = "SELECT * FROM profil WHERE id_compte = :id_compte;";
$stmt = $pdo->prepare($sql);
$stmt->execute(['id_compte' => $user['id']]);
$profils = $stmt->fetchAll(PDO::FETCH_ASSOC);
?>


<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
        <link rel="stylesheet" href="assets/css/style.css">
        <title>Netflux</title>
    </head>

    <body id="page_accueil">
        <header>
            <h1>Qui est-ce ?</h1>
        </header>

        <div id="profils">
            <ul>
                <?php foreach ($profils as $profil) : ?>
                    <li>
                        <a href="profil.php">
                            <img src="<?= htmlspecialchars($profil['img']); ?>" alt="profil1">
                            <span><?= htmlspecialchars($profil['nom']); ?></span>
                        </a>
                    </li>
                <?php endforeach; ?>
            </ul>
        </div>
    </body>
</html>
