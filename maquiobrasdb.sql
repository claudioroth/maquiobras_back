-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: May 09, 2024 at 03:20 PM
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
  `fecha` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `control`
--

INSERT INTO `control` (`id`, `id_user`, `id_prod`, `retiro`, `fecha`) VALUES
(1, 3, 1, 2, '2023-11-30 11:30:00'),
(2, 3, 1, 1, '2023-11-30 11:32:00'),
(3, 1, 4, 1, '2023-12-06 12:39:23'),
(4, 1, 1, 5, '2023-12-07 08:53:17'),
(5, 1, 2, 10, '2023-12-07 08:53:25'),
(6, 1, 1, 25, '2023-12-07 08:54:01'),
(7, 1, 1, 25, '2023-12-07 08:54:11'),
(8, 1, 1, 25, '2023-12-07 08:54:12'),
(9, 1, 1, 25, '2023-12-07 08:54:13'),
(10, 1, 1, 25, '2023-12-07 08:54:14');

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `id` int(11) NOT NULL,
  `nombre_prod` varchar(50) NOT NULL,
  `tipo_prod` varchar(20) NOT NULL,
  `cantidad` int(255) NOT NULL,
  `descripcion` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`id`, `nombre_prod`, `tipo_prod`, `cantidad`, `descripcion`) VALUES
(1, 'martillo', 'heramienta', 10, 'martillo de goma'),
(2, 'tornillos 1', 'accesorio', 2, 'tornillos medida 1'),
(3, 'tornillos 2', 'accesorio', 5, 'tornillos medida 2'),
(4, 'destornillador 1', 'accesorio', 10, 'destornillador medida 1');

-- --------------------------------------------------------

--
-- Table structure for table `product_detail`
--

CREATE TABLE `product_detail` (
  `index` bigint(20) DEFAULT NULL,
  `N°` text,
  `VENTA + 1/2 IVA` double DEFAULT NULL,
  `DESCRIPCION` text,
  `LISTA VIEJA` double DEFAULT NULL,
  `IMPORTE` bigint(20) DEFAULT NULL,
  `C/IVA 21%` text,
  `C/IVA 10.5%` double DEFAULT NULL,
  `OFERTA SIN IVA` bigint(20) DEFAULT NULL,
  `AUMENTO` datetime DEFAULT NULL,
  `ULT.MODIF.` datetime DEFAULT NULL,
  `PROV.1` double DEFAULT NULL,
  `PROV.2` double DEFAULT NULL,
  `PROV.3` double DEFAULT NULL,
  `OFERTA` double DEFAULT NULL,
  `COSTO MAS BAJO` double DEFAULT NULL,
  `COSTO MAS BAJO.1` double DEFAULT NULL,
  `RENTAB.` double DEFAULT NULL,
  `VENTA` double DEFAULT NULL,
  `Unnamed: 18` double DEFAULT NULL,
  `VENTA OFERTA` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `product_detail`
--

INSERT INTO `product_detail` (`index`, `N°`, `VENTA + 1/2 IVA`, `DESCRIPCION`, `LISTA VIEJA`, `IMPORTE`, `C/IVA 21%`, `C/IVA 10.5%`, `OFERTA SIN IVA`, `AUMENTO`, `ULT.MODIF.`, `PROV.1`, `PROV.2`, `PROV.3`, `OFERTA`, `COSTO MAS BAJO`, `COSTO MAS BAJO.1`, `RENTAB.`, `VENTA`, `Unnamed: 18`, `VENTA OFERTA`) VALUES
(0, '19 21', NULL, 'ABRAZADERA PLASTICA 100 x 2,5 ABR1100', 70, 1000, '1210', NULL, 0, '2023-10-18 00:00:00', '2023-12-11 00:00:00', NULL, 495.423, NULL, NULL, 495.423, 495.423, 2, 990.846, NULL, 0),
(1, '19 21', NULL, 'ABRAZADERA PLASTICA 150 x 3,6 ABR1160', 160, 2370, '2867.7', NULL, 0, '2023-10-18 00:00:00', '2023-12-11 00:00:00', NULL, 1184.1299999999999, NULL, NULL, 1184.1299999999999, 1184.1299999999999, 2, 2368.2599999999998, NULL, 0),
(2, '12', NULL, 'ABRAZADERA PLASTICA 250 X 3,6 900006', 300, 5170, '6255.7', NULL, 0, '2024-01-23 00:00:00', NULL, 2585, NULL, NULL, NULL, 2585, 2585, 2, 5170, NULL, 0),
(3, '19 21 45', NULL, 'ABRAZADERA PLASTICA 250 X 4,8 900011', 300, 6800, '8228', NULL, 0, '2024-01-23 00:00:00', NULL, 3399, NULL, NULL, NULL, 3399, 3399, 2, 6798, NULL, 0),
(4, '19 21', NULL, 'ABRAZADERA PLASTICA 300 x 3,6 ABR 2250', 360, 6590, '7973.9', NULL, 0, '2023-10-18 00:00:00', '2023-12-11 00:00:00', NULL, 3292.2000000000003, NULL, NULL, 3292.2000000000003, 3292.2000000000003, 2, 6584.400000000001, NULL, 0),
(5, '19 21 45', NULL, 'ABRAZADERA PLASTICA 300 x 4,6 ABR 3036', 860, 6360, '7695.599999999999', NULL, 0, '2023-10-18 00:00:00', '2023-12-11 00:00:00', NULL, 3175.38, NULL, NULL, 3175.38, 3175.38, 2, 6350.76, NULL, 0),
(6, NULL, NULL, 'ACEITE MOBIL SUPER MOTO 4 T 20W -50 x 1 LT', 300, 5880, '7114.8', NULL, 0, '2023-08-19 00:00:00', NULL, 3456.48, NULL, NULL, NULL, 3456.48, 3456.48, 1.7, 5876.016, NULL, 0),
(7, '52', NULL, 'ACEITE SHIMURA x 1 LITRO', 300, 7820, '9462.199999999999', NULL, 0, '2021-07-08 00:00:00', '2024-02-16 00:00:00', 5207.40801875, NULL, NULL, NULL, 5207.40801875, 5207.40801875, 1.5, 7811.1120281250005, NULL, 0),
(8, '16', NULL, 'ACOPLE HEMBRA MOTOR VIBRADOR FLEXI', 880, 52950, '64069.5', NULL, 0, NULL, '2024-02-23 00:00:00', 35300, NULL, NULL, NULL, 35300, 35300, 1.5, 52950, NULL, 0),
(9, '41', NULL, 'ACOPLE HEMBRA MOTOR VIBRADOR MMQ', 1040, 19010, '23002.1', NULL, 0, NULL, '2024-02-28 00:00:00', 11877, NULL, NULL, NULL, 11877, 11877, 1.6, 19003.2, NULL, 0),
(10, '16', NULL, 'ACOPLE MACHO MANGUERA VIBRADOR FLEXI', 760, 0, '0', NULL, 0, '2023-05-08 00:00:00', NULL, 7445.721690000002, NULL, NULL, NULL, 7445.721690000002, 7445.721690000002, NULL, 0, NULL, 0),
(11, '41', NULL, 'ACOPLE MACHO MANGUERA VIBRADOR MMQ', 870, 16950, '20509.5', NULL, 0, NULL, '2024-02-28 00:00:00', 10593, NULL, NULL, NULL, 10593, 10593, 1.6, 16948.8, NULL, 0),
(12, '24', NULL, 'ADAPTADOR SDS A MANDRIL ISARD 109530', NULL, 1790, '2165.9', NULL, 0, '2023-09-06 00:00:00', NULL, 1187.2, NULL, NULL, NULL, 1187.2, 1187.2, 1.5, 1780.8000000000002, NULL, 0),
(13, '38', NULL, 'ADAPTADOR SDS A MANDRIL GLADIATOR GLAM800', NULL, 850, '1028.5', NULL, 0, '2023-09-04 00:00:00', NULL, 528, NULL, NULL, NULL, 528, 528, 1.6, 844.8000000000001, NULL, 0),
(14, '38', NULL, 'ADAPTADOR SDS A MANDRIL MAKITA MKT14087', 90, 1980, '2395.7999999999997', NULL, 0, '2023-09-04 00:00:00', NULL, 1314, NULL, NULL, NULL, 1314, 1314, 1.5, 1971, NULL, 0),
(15, NULL, 500710, 'ADIABATIC EC2000NEW_TG', 19880, 472360, '*', 521957.8, 0, '2024-03-07 00:00:00', NULL, 337397, NULL, NULL, NULL, 337397, 337397, 1.4, 472355.8, NULL, 0),
(16, NULL, 688890, 'ADIABATIC EC3000NEW ', 19880, 649890, '*', 718128.45, 0, '2024-03-07 00:00:00', NULL, 464202, NULL, NULL, NULL, 464202, 464202, 1.4, 649882.7999999999, NULL, 0),
(17, '87', NULL, 'AFILADO DE PUNTA/CORTA 11304', 190, 1400, '1694', NULL, 0, '2024-03-26 00:00:00', NULL, 700, NULL, NULL, NULL, 700, 700, 2, 1400, NULL, 0),
(18, '87', NULL, 'AFILADO DE PUNTA/CORTA SDS MAX', 170, 1300, '1573', NULL, 0, '2024-03-26 00:00:00', NULL, 650, NULL, NULL, NULL, 650, 650, 2, 1300, NULL, 0),
(19, '87', NULL, 'AFILADO JABALINA', NULL, 0, NULL, NULL, 0, NULL, NULL, 190, NULL, NULL, NULL, 190, 190, NULL, 0, NULL, 0),
(20, '10', 0, 'ALAMBRE DE FARDO 15 1,8 MM A GRANEL POR 65 KG ACINDAR (AN15V)', NULL, 0, '0', NULL, 0, '2022-06-09 00:00:00', '2022-07-26 00:00:00', 28509, NULL, NULL, NULL, 28509, 28509, NULL, 0, NULL, 0),
(21, '10 21 71', 0, 'ALAMBRE DE FARDO 16 1,6 MM A GRANEL POR 65 KG ACINDAR (AN16V)', 11350, 0, '0', NULL, 0, '2022-06-09 00:00:00', '2022-07-26 00:00:00', 29794.7, NULL, NULL, NULL, 29794.7, 29794.7, NULL, 0, NULL, 0),
(22, '103', 262450, 'ALAMBRE DE FARDO 16 1,6 MM A GRANEL POR 65 KG HERPACO', NULL, 237510, '287387.1', NULL, 214330, NULL, '2024-02-23 00:00:00', 163800, NULL, NULL, 147810, 163800, 163800, 1.45, 237510, NULL, 214324.5),
(23, '103', 0, 'ALAMBRE DE FARDO 17 1,42 MM A GRANEL POR 50 KG HERPACO', NULL, 0, '0', NULL, 0, NULL, '2023-01-09 00:00:00', 25700, NULL, NULL, NULL, 25700, 25700, NULL, 0, NULL, 0),
(24, '10', 0, 'ALAMBRE DE FARDO 17 1,42 MM A GRANEL POR 65 KG ACINDAR (an17v) ', NULL, 0, '0', NULL, 0, '2022-06-09 00:00:00', '2022-07-26 00:00:00', 31751.2, NULL, NULL, NULL, 31751.2, 31751.2, NULL, 0, NULL, 0),
(25, '19 21', 4570, 'ALAMBRE DE FARDO POR 1 KG SIP16', 200, 4130, '4997.3', NULL, 3750, '2023-10-18 00:00:00', '2024-03-25 00:00:00', 2750.58, NULL, NULL, 2495.7000000000003, 2750.58, 2750.58, 1.5, 4125.87, NULL, 3743.55),
(26, '10 21 71', 0, 'ALAMBRE NEGRO RECOCIDO N° 8 DEL 4,2 POR 60 KG (AN8V)', 10960, 0, '0', NULL, 0, '2022-06-09 00:00:00', '2022-07-26 00:00:00', 26664.3, 227039.67000000004, NULL, NULL, 26664.3, 26664.3, NULL, 0, NULL, 0),
(27, '103', 238910, 'ALAMBRE NEGRO RECOCIDO N° 8 DEL 4,2 POR 60 KG HERPACO', NULL, 216200, '261602', NULL, 195150, NULL, '2024-02-23 00:00:00', 149100, NULL, NULL, 134580, 149100, 149100, 1.45, 216195, NULL, 195141);

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
(1, 'admin', 'admin', 1, 1, '2024-05-08 15:43:24'),
(2, 'pato', 'soyadmin', 1, 1, '2023-11-30 11:06:35'),
(3, 'carlos', '12345', 0, 1, '2023-11-30 11:06:35');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `control`
--
ALTER TABLE `control`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `product_detail`
--
ALTER TABLE `product_detail`
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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `provedor`
--
ALTER TABLE `provedor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
