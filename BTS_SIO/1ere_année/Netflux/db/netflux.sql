SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

CREATE DATABASE IF NOT EXISTS netflux;
USE netflux;

--
-- Base de données : `netflux`
--

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

CREATE TABLE `users` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `login` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `mdp` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `users`
--

INSERT INTO `users` (`id`, `login`, `mdp`) VALUES
(1, 'toto@example.com', 'password'),
(2, 'titi@example.com', 'password123'),
(3, 'tutu@example.com', 'Password123');


--
-- Structure de la table `users`
--

CREATE TABLE `profil` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `id_compte` bigint(20) UNSIGNED NOT NULL,
  `nom` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `img` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `users`
--

INSERT INTO `users` (`id`, `id_compte`, `nom`, `img`) VALUES
(1, '1', 'Toto', `assets/image/profile_icons/profile_icon1.png`),
(2, '1', 'Jean-Jacques', `assets/image/profile_icons/profile_icon2.png`),
(3, '2', 'Titi', `assets/image/profile_icons/profile_icon1.png`),
(4, '2', 'Gros Minet', `assets/image/profile_icons/profile_icon4.png`),
(5, '3', 'Maxime', `assets/image/profile_icons/profile_icon4.png`),
(6, '3', 'Pierre', `assets/image/profile_icons/profile_icon1.png`),
(7, '3', 'Victor', `assets/image/profile_icons/profile_icon2.png`),
(8, '3', 'Yoann', `assets/image/profile_icons/profile_icon3.png`),

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `users_login_unique` (`login`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `users`
--
ALTER TABLE `users`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;