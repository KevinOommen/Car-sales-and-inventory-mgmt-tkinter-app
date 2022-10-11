-- MySQL dump 10.13  Distrib 5.7.29, for Win64 (x86_64)
--
-- Host: localhost    Database: projectdb
-- ------------------------------------------------------
-- Server version	5.7.29-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customers` (
  `NAME` varchar(25) DEFAULT NULL,
  `phone` bigint(12) DEFAULT NULL,
  `EMAIL` varchar(35) NOT NULL,
  `ADDR` varchar(80) NOT NULL,
  `PUR_DATE` date NOT NULL,
  `PLATE` varchar(12) DEFAULT NULL,
  `RESVAL` int(7) DEFAULT NULL,
  `INVNO` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`INVNO`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES ('Ryan',741852963,'ryan@gmail.com','Kochi','2020-11-10','KL 12 A 1234',10000000,1),('KEvin',1234567890,'','','2020-11-11','KL 27 B 1234',4500000,2),('Jake',8213456970,'jake@gmail.com','THiruvalla\nnear more','2020-11-11','KA 23 B 1234',0,3),('John Abraham',8521346790,'johanabram@yahoo.com','Banyan Villa,\nChengannur,\nWest P.O.','2021-01-08','KL 27 A 4321',0,5),('Tony Johnson',7895623410,'tonyjson@gmail.com','Shreyas Bhavan,\nMathilbhagom,\nThiruvalla','2021-01-09','KA 35 B 7845',1300000,6),('A',1234567890,'@gmail','a','2021-01-09','GA 23 A 1234',2000000,7),('A',1234567890,'@','Hello','2021-01-09','GA 23 A 1234',2000000,8);
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `username` varchar(20) DEFAULT NULL,
  `password` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('Kevin ','ironman'),('Adarsh','vergis');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vehicles`
--

DROP TABLE IF EXISTS `vehicles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vehicles` (
  `BRAND` varchar(13) NOT NULL,
  `MODEL` varchar(12) NOT NULL,
  `YEARB` int(4) NOT NULL,
  `VAR` varchar(16) NOT NULL,
  `YEARP` int(4) NOT NULL,
  `STATE` varchar(17) NOT NULL,
  `PRICE` int(8) NOT NULL,
  `COLOR` varchar(20) DEFAULT NULL,
  `PLATE` varchar(12) NOT NULL,
  `TRIP` int(7) NOT NULL,
  `RESVAL` int(7) DEFAULT NULL,
  `NAME` varchar(25) NOT NULL,
  `phone` bigint(12) DEFAULT NULL,
  `EMAIL` varchar(35) NOT NULL,
  `ADDR` varchar(80) NOT NULL,
  `AVAIL` varchar(8) NOT NULL,
  PRIMARY KEY (`PLATE`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehicles`
--

LOCK TABLES `vehicles` WRITE;
/*!40000 ALTER TABLE `vehicles` DISABLE KEYS */;
INSERT INTO `vehicles` VALUES ('FORD','FIGO',2010,'1.4LX DURATORQ',2011,'GA-GOA',2500000,'GREE','GA 23 A 1234',1000,200000,'Q',1245789630,'q@gmail','q','sold'),('FORD','ENDEAVOUR',2019,'2.5 4X4',2020,'KA-KARNATAKA',5000000,'BLUE','KA 23 B 1234',5000,0,'BLAKE',7894561230,'blake@gmail.com','THiruvalla,\nKuttapuzha,\nnear mTRS','sold'),('MARUTI SUZUKI','WAGON R',2017,'VXI',2019,'KA-KARNATAKA',1300000,'RED','KA 35 B 7845',4500,0,'ROSHANANDREWS',7845129630,'roshanandrews@outlook.com','House no.121,\nGandhi Nagar Street,\nKarnataka','sold'),('MARUTI SUZUKI','SWIFT DEZIRE',2011,'LDI',2012,'KL-KERALA',1200000,'WHITE','KL 12 A 1234',2000,1000000,'KEVIN OOMMEN',1234567890,'kevino@gmail.com','Parelpally,\nChangnaserry\nKottayam','sold'),('TOYOTA','INNNOVA',2012,'2.0 VX 7',2013,'KL-KERALA',2500000,'BLUE','KL 21 A 1245',3000,2000000,'ADARSH VARGHESE',1245789630,'adarshv@gmail.com','City Apartments,\nParelpally,\nChangnaserry','sold'),('MARUTI SUZUKI','WAGON R',2018,'ZDX',2019,'KL-KERALA',1200000,'BLUE','KL 27 A 4321',2000,0,'JOHAN',1234567890,'johan@gmail.com','Thiruvalla,\nKuttapuzha','sold'),('FORD','FIGO',2018,'1.4LXI DURATORQ',2020,'KL-KERALA',300000,'WHITE','KL 27 B 1234',500,450000,'ADARSH VARGHESE',1234567890,'adarshvergis@gmail.com','Sowparnika Apartments\nParelpally,\nChangnaserry','sold');
/*!40000 ALTER TABLE `vehicles` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-01-15  3:49:47
