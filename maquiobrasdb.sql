-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Jun 03, 2024 at 09:01 PM
-- Server version: 5.7.39
-- PHP Version: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `maquiobrasdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `control`
--

CREATE TABLE `control` (
  `id` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `id_prod` int(11) NOT NULL,
  `retiro` int(11) NOT NULL,
  `fecha` datetime NOT NULL,
  `local` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `control`
--

INSERT INTO `control` (`id`, `id_user`, `id_prod`, `retiro`, `fecha`, `local`) VALUES
(1, 1, 1, 1, '2024-06-03 10:58:57', 'Deposito'),
(2, 1, 1, 1, '2024-06-03 11:01:10', 'Deposito'),
(3, 1, 49, 1, '2024-06-03 11:02:30', 'Galicia');

-- --------------------------------------------------------

--
-- Table structure for table `product_detail`
--

CREATE TABLE `product_detail` (
  `index` bigint(20) NOT NULL,
  `N° PROV.` text,
  `DESCRIPCION` text,
  `IMPORTE S/IVA` bigint(20) DEFAULT NULL,
  `C/IVA 21%` text,
  `C/IVA 10.5%` double DEFAULT NULL,
  `OFERTA SIN IVA` bigint(20) DEFAULT NULL,
  `AUMENTO` datetime DEFAULT NULL,
  `ULT.MODIF.` datetime DEFAULT NULL,
  `OFERTA COSTO` double DEFAULT NULL,
  `COSTO MAS BAJO` double DEFAULT NULL,
  `RENTAB.` double DEFAULT NULL,
  `STOCK` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `product_detail`
--

INSERT INTO `product_detail` (`index`, `N° PROV.`, `DESCRIPCION`, `IMPORTE S/IVA`, `C/IVA 21%`, `C/IVA 10.5%`, `OFERTA SIN IVA`, `AUMENTO`, `ULT.MODIF.`, `OFERTA COSTO`, `COSTO MAS BAJO`, `RENTAB.`, `STOCK`) VALUES
(1, '19 21', 'ABRAZADERA PLASTICA 100 x 2,5 ABR1100', 0, '0', NULL, 0, '2023-10-18 00:00:00', '2023-12-11 00:00:00', NULL, 0, 2, 11),
(2, '19 21', 'ABRAZADERA PLASTICA 150 x 3,6 ABR1160', 0, '0', NULL, 0, '2023-10-18 00:00:00', '2023-12-11 00:00:00', NULL, 0, 2, 22),
(3, '12', 'ABRAZADERA PLASTICA 250 X 3,6 900006', 5170, '6255.7', NULL, 0, '2024-01-23 00:00:00', NULL, NULL, 2585, 2, 1),
(4, '19 21 45', 'ABRAZADERA PLASTICA 250 X 4,8 900011', 6800, '8228', NULL, 0, '2024-01-23 00:00:00', NULL, NULL, 3399, 2, NULL),
(5, '19 21', 'ABRAZADERA PLASTICA 300 x 3,6 ABR 2250', 0, '0', NULL, 0, '2023-10-18 00:00:00', '2023-12-11 00:00:00', NULL, 0, 2, NULL),
(6, '19 21 45', 'ABRAZADERA PLASTICA 300 x 4,6 ABR 3036', 0, '0', NULL, 0, '2023-10-18 00:00:00', '2023-12-11 00:00:00', NULL, 0, 2, NULL),
(7, '36', 'ACANALADORA DE MURO TE-MA 1500 4350735', 362400, '*', 400452, 0, NULL, '2024-02-28 00:00:00', NULL, 258855.9789024, 1.4, NULL),
(8, '36', 'ACANALADORA DE MURO TH-MA 1300 4350731', 281200, '*', 310726, 0, NULL, '2024-02-28 00:00:00', NULL, 200853.7257408, 1.4, NULL),
(9, NULL, 'ACEITE MOBIL SUPER MOTO 4 T 20W -50 x 1 LT', 5880, '7114.8', NULL, 0, '2023-08-19 00:00:00', NULL, NULL, 3456.48, 1.7, NULL),
(10, '52', 'ACEITE SHIMURA x 1 LITRO', 8190, '9909.9', NULL, 0, '2021-07-08 00:00:00', '2024-02-16 00:00:00', NULL, 5455.379829166667, 1.5, NULL),
(11, '16', 'ACOPLE HEMBRA MOTOR VIBRADOR FLEXI', 52950, '64069.5', NULL, 0, NULL, '2024-02-23 00:00:00', NULL, 35300, 1.5, NULL),
(12, '41', 'ACOPLE HEMBRA MOTOR VIBRADOR MMQ', 19010, '23002.1', NULL, 0, NULL, '2024-02-28 00:00:00', NULL, 11877, 1.6, NULL),
(13, '16', 'ACOPLE MACHO MANGUERA VIBRADOR FLEXI', 0, '0', NULL, 0, '2023-05-08 00:00:00', NULL, NULL, 7445.721690000002, NULL, NULL),
(14, '41', 'ACOPLE MACHO MANGUERA VIBRADOR MMQ', 16950, '20509.5', NULL, 0, NULL, '2024-02-28 00:00:00', NULL, 10593, 1.6, NULL),
(15, '38', 'ADAPTADOR SDS A MANDRIL GLADIATOR GLAM800', 850, '1028.5', NULL, 0, '2023-09-04 00:00:00', NULL, NULL, 528, 1.6, NULL),
(16, '24', 'ADAPTADOR SDS A MANDRIL ISARD 109530', 1790, '2165.9', NULL, 0, '2023-09-06 00:00:00', NULL, NULL, 1187.2, 1.5, NULL),
(17, '38', 'ADAPTADOR SDS A MANDRIL MAKITA MKT14087', 1980, '2395.7999999999997', NULL, 0, '2023-09-04 00:00:00', NULL, NULL, 1314, 1.5, NULL),
(18, NULL, 'ADIABATIC EC2000NEW_TG', 472360, '*', 521957.8, 0, '2024-03-07 00:00:00', NULL, NULL, 337397, 1.4, NULL),
(19, NULL, 'ADIABATIC EC3000NEW ', 649890, '*', 718128.45, 0, '2024-03-07 00:00:00', NULL, NULL, 464202, 1.4, NULL),
(20, '87', 'AFILADO DE PUNTA/CORTA 11304', 2200, '2662', NULL, 0, '2024-04-24 00:00:00', NULL, NULL, 1100, 2, NULL),
(21, '87', 'AFILADO DE PUNTA/CORTA SDS MAX', 1900, '2299', NULL, 0, '2024-04-24 00:00:00', NULL, NULL, 950, 2, NULL),
(22, '87', 'AFILADO JABALINA', 0, NULL, NULL, 0, NULL, NULL, NULL, 190, NULL, NULL),
(23, '10', 'ALAMBRE DE FARDO 15 1,8 MM A GRANEL POR 65 KG ACINDAR (AN15V)', 0, '0', NULL, 0, '2022-06-09 00:00:00', '2022-07-26 00:00:00', NULL, 28509, NULL, NULL),
(24, '10 21 71', 'ALAMBRE DE FARDO 16 1,6 MM A GRANEL POR 65 KG ACINDAR (AN16V)', 0, '0', NULL, 0, '2022-06-09 00:00:00', '2022-07-26 00:00:00', NULL, 29794.7, NULL, NULL),
(25, '103', 'ALAMBRE DE FARDO 16 1,6 MM A GRANEL POR 65 KG HERPACO', 237510, '287387.1', NULL, 222720, NULL, '2024-04-25 00:00:00', 153595, 163800, 1.45, NULL),
(26, '103', 'ALAMBRE DE FARDO 17 1,42 MM A GRANEL POR 50 KG HERPACO', 0, '0', NULL, 0, NULL, '2023-01-09 00:00:00', NULL, 25700, NULL, NULL),
(27, '10', 'ALAMBRE DE FARDO 17 1,42 MM A GRANEL POR 65 KG ACINDAR (an17v) ', 0, '0', NULL, 0, '2022-06-09 00:00:00', '2022-07-26 00:00:00', NULL, 31751.2, NULL, NULL),
(28, '19 21', 'ALAMBRE DE FARDO POR 1 KG SIP16', 4250, '5142.5', NULL, 3850, '2023-10-18 00:00:00', '2024-05-16 00:00:00', 2566.2000000000003, 2828.2799999999997, 1.5, NULL),
(29, '10 21 71', 'ALAMBRE NEGRO RECOCIDO N° 8 DEL 4,2 POR 60 KG (AN8V)', 0, '0', NULL, 0, '2022-06-09 00:00:00', '2022-07-26 00:00:00', NULL, 26664.3, NULL, NULL),
(30, '103', 'ALAMBRE NEGRO RECOCIDO N° 8 DEL 4,2 POR 60 KG HERPACO', 216200, '261602', NULL, 202890, NULL, '2024-04-25 00:00:00', 139920, 149100, 1.45, NULL),
(31, '103', 'ALAMBRON 6,00 MM POR 100 KG HERPACO', 232150, '280901.5', NULL, 214020, NULL, '2024-04-25 00:00:00', 147600, 160100, 1.45, NULL),
(32, '103', 'ALAMBRON 6,00 MM POR 50 KG HERPACO', 116080, '140456.8', NULL, 107010, NULL, '2024-04-25 00:00:00', 73800, 80050, 1.45, NULL),
(33, '10', 'ALAMBRON 6,00 MM POR 80 KG (AON600V)', 0, '0', NULL, 0, '2022-06-09 00:00:00', '2022-07-26 00:00:00', NULL, 0, NULL, NULL),
(34, '36', 'ALCOHOL EN AEROSOL AL 70 % ', 0, '0', NULL, 0, NULL, '2021-04-22 00:00:00', NULL, 152.656, NULL, NULL),
(35, '36', 'ALCOHOL EN GEL x 5 LTS ITURRIA (OFERTA OTRO)', 0, '0', NULL, 0, '2022-12-12 00:00:00', NULL, 1500, 2995.968, NULL, NULL),
(36, NULL, 'ALCOHOL ETANOL AL 70 % x 250 CC', 0, '0', NULL, 0, '2022-04-26 00:00:00', NULL, NULL, 100, NULL, NULL),
(37, '36', 'ALCOHOL ETANOL AL 70 % x 5 LTS ITURRIA (OFERTA OTRO)', 0, '0', NULL, 0, '2022-12-12 00:00:00', NULL, 1400, 2610.192, NULL, NULL),
(38, '13', 'ALIAFOR Abrasivo Extra Ø 12\" - Sector 9 mm - Super Supreme - Ø Interior 25,4 mm S12AX9SSP', 294080, '355836.8', NULL, 0, NULL, '2024-02-01 00:00:00', NULL, 202811.72593499997, 1.45, NULL),
(39, '13', 'ALIAFOR Abrasivo Extra Ø 12\" - Sector 9 mm - Super Supreme - Ø Interior 50 mm L12AX9SSP', 294080, '355836.8', NULL, 0, NULL, '2024-02-01 00:00:00', NULL, 202811.72593499997, 1.45, NULL),
(40, '13', 'ALIAFOR Abrasivo Extra Ø 14\" - Sector 9 mm - Super Supreme Plus - Ø Interior 25,4 mm S14AX9SSP', 324410, '392536.1', NULL, 0, NULL, '2024-02-01 00:00:00', NULL, 223725.1653, 1.45, NULL),
(41, '13', 'ALIAFOR Abrasivo Extra Ø 14\" - Sector 9 mm - Super Supreme Plus - Ø Interior 50 mm L14AX9SSP', 324410, '392536.1', NULL, 0, NULL, '2024-02-01 00:00:00', NULL, 223725.1653, 1.45, NULL),
(42, '13', 'ALIAFOR Abrasivo Extra Ø 16\" - Sector 9 mm - Super Supreme - Ø Interior 25,4 mm S16AX9SSP', 415730, '503033.3', NULL, 0, NULL, '2024-02-01 00:00:00', NULL, 286708.6629225, 1.45, NULL),
(43, '13', 'ALIAFOR Abrasivo Extra Ø 16\" - Sector 9 mm - Super Supreme - Ø Interior 50 mm L16AX9SSP', 415730, '503033.3', NULL, 0, NULL, '2024-02-01 00:00:00', NULL, 286708.6629225, 1.45, NULL),
(44, '13', 'ALIAFOR Abrasivo Extra Ø 18\" - Sector 9 mm - Super Supreme - Ø Interior 25,4 mm S18AX9SSP', 507760, '614389.6', NULL, 0, NULL, '2024-02-01 00:00:00', NULL, 350178.5196, 1.45, NULL),
(45, '13', 'ALIAFOR Abrasivo Extra Ø 18\" - Sector 9 mm - Super Supreme - Ø Interior 50 mm L18AX9SSP', 507760, '614389.6', NULL, 0, NULL, '2024-02-01 00:00:00', NULL, 350178.5196, 1.45, NULL),
(46, '13', 'ALIAFOR Abrasivo Extra Ø 20\" - Sector 10 mm - Super Supreme - Ø Interior 25,4 mm S20AX10SSP', 566300, '685223', NULL, 0, NULL, '2024-02-01 00:00:00', NULL, 390546.321165, 1.45, NULL),
(47, '13', 'ALIAFOR Abrasivo Extra Ø 20\" - Sector 10 mm - Super Supreme - Ø Interior 50 mm L20AX10SSP', 566300, '685223', NULL, 0, NULL, '2024-02-01 00:00:00', NULL, 390546.321165, 1.45, NULL),
(48, '13', 'ALIAFOR Abrasivo Extra Ø 24\" - Sector 9 mm - Super Supreme - Ø Interior 60 mm L24AX10SSP', 794790, '961695.9', NULL, 0, NULL, '2024-02-01 00:00:00', NULL, 548126.6549849999, 1.45, NULL),
(49, '13', 'ALIAFOR Abrasivo Ø 12\" - Sector 10 mm - Supreme Supreme Plus - Ø Interior 25,4 mm. S12A10SSP', 265520, '321279.2', NULL, 0, NULL, '2024-02-01 00:00:00', NULL, 183114.1842075, 1.45, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `provedor`
--

CREATE TABLE `provedor` (
  `id` int(11) NOT NULL,
  `prov_id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `provedor`
--

INSERT INTO `provedor` (`id`, `prov_id`, `nombre`) VALUES
(1, 10, 'ABACO'),
(2, 11, 'ABASTECER SEGURIDAD'),
(3, 12, 'ALFREDO ALVAREZ'),
(4, 13, 'ALIAFOR'),
(5, 14, 'ALSEC'),
(6, 15, 'ANCLAJES Y SERVICIOS'),
(7, 16, 'APEZTEGUIA'),
(8, 17, 'BAEZ'),
(9, 18, 'BOSH'),
(10, 19, 'CAMITS'),
(11, 20, 'CASA LEON'),
(12, 21, 'CASA LOUREIRO'),
(13, 22, 'CATINARI');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `user` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `is_admin` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `fecha` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `user`, `password`, `is_admin`, `is_active`, `fecha`) VALUES
(1, 'admin', 'admin', 1, 1, '2024-05-30 22:46:57'),
(2, 'pato', 'soyadmin', 1, 1, '2024-05-11 12:17:43'),
(3, 'carlos', '12345', 0, 0, '2024-05-14 19:04:43');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `control`
--
ALTER TABLE `control`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `product_detail`
--
ALTER TABLE `product_detail`
  ADD PRIMARY KEY (`index`),
  ADD KEY `ix_product_detail_index` (`index`);

--
-- Indexes for table `provedor`
--
ALTER TABLE `provedor`
  ADD UNIQUE KEY `prov_id` (`prov_id`),
  ADD KEY `id` (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `control`
--
ALTER TABLE `control`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `product_detail`
--
ALTER TABLE `product_detail`
  MODIFY `index` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=50;

--
-- AUTO_INCREMENT for table `provedor`
--
ALTER TABLE `provedor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
