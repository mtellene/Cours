<?php
// Database connection settings
$host = '127.0.0.1';
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
    $login = trim($_POST['name']);
    $mdp = trim($_POST['mdp']);

    if (!empty($login) && !empty($mdp) && !empty($mdp)) {
        try {
            // Insert data into the database
            $sql = "INSERT INTO users (login, mdp) VALUES (:login, :mdp)";
            $stmt = $pdo->prepare($sql);
            $stmt->execute(['login' => $login, 'mdp' => $mdp]);
            $successMessage = "Registration successful!";
        } catch (PDOException $e) {
            $errorMessage = "Error: " . $e->getMessage();
        }
    } else {
        $errorMessage = "Please enter a valid name and email.";
    }
}
?>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Accueil - Netflux</title>
</head>
<body>

    <h2>Connexion</h2>

    <?php if ($successMessage): ?>
        <p style="color: green;"><?php echo $successMessage; ?></p>
    <?php endif; ?>

    <?php if ($errorMessage): ?>
        <p style="color: red;"><?php echo $errorMessage; ?></p>
    <?php endif; ?>

    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" value="<?php echo htmlspecialchars($name); ?>" required>
        <br><br>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" value="<?php echo htmlspecialchars($email); ?>" required>
        <br><br>

        <button type="submit">Submit</button>
    </form>

</body>
</html>
