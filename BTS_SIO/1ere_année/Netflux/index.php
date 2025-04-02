<?php
// Database connection settings
$host = 'netflux-db';
$dbname = 'netflux';
$username = 'netuser';
$password = 'netpass';

try {
    // Connect to the database
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Initialize variables
$login = $mdp = "";
$successMessage = $errorMessage = "";

// Handle form submission
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $login = trim($_POST['login']);
    $mdp = trim($_POST['mdp']);

    if (!empty($login) && !empty($mdp)) {
        try {
            // Insert data into the database
            $sql = "SELECT * FROM users WHERE login = :login AND mdp = :mdp";
            $stmt = $pdo->prepare($sql);
            $stmt->execute(['login' => $login, 'mdp' => $mdp]);

            $user = $stmt->fetch(PDO::FETCH_ASSOC);
            if ($user){
                session_start();
                $_SESSION['user'] = $user;
                header("Location: choix_profil.php");
                exit();
            } else {
                $errorMessage = "Invalid login or password";
            }
        } catch (PDOException $e) {
            $errorMessage = "Error: " . $e->getMessage();
        }
    } else {
        $errorMessage = "Connection error: bad login or password";
    }
}
?>

<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="assets/css/style.css">
        <title>Accueil - Netflux</title>
    </head>
    <body>
        <h2>Connexion</h2>

        <?php if ($errorMessage): ?>
            <p style="color: red;"><?php echo $errorMessage; ?></p>
        <?php endif; ?>

        <form method="post">
            <label for="login">Login :</label>
            <input type="text" id="login" name="login" value="" required>
            <br><br>

            <label for="mdp">Mot de passe :</label>
            <input type="password" id="mdp" name="mdp" value="" required>
            <br><br>

            <button type="submit">Submit</button>
        </form>
    </body>
</html>

