CREATE DATABASE  IF NOT EXISTS `cartelera` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `cartelera`;
-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: cartelera
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `asientos`
--

DROP TABLE IF EXISTS `asientos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `asientos` (
  `id_asiento` int NOT NULL AUTO_INCREMENT,
  `numero_asiento` tinyint unsigned NOT NULL,
  `id_sala` int NOT NULL,
  PRIMARY KEY (`id_asiento`),
  KEY `fk_asiento_sala1_idx` (`id_sala`),
  CONSTRAINT `fk_asiento_sala1` FOREIGN KEY (`id_sala`) REFERENCES `sala` (`id_sala`)
) ENGINE=InnoDB AUTO_INCREMENT=301 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asientos`
--

LOCK TABLES `asientos` WRITE;
/*!40000 ALTER TABLE `asientos` DISABLE KEYS */;
INSERT INTO `asientos` VALUES (1,1,1),(2,2,1),(3,3,1),(4,4,1),(5,5,1),(6,6,1),(7,7,1),(8,8,1),(9,9,1),(10,10,1),(11,11,1),(12,12,1),(13,13,1),(14,14,1),(15,15,1),(16,16,1),(17,17,1),(18,18,1),(19,19,1),(20,20,1),(21,21,1),(22,22,1),(23,23,1),(24,24,1),(25,25,1),(26,26,1),(27,27,1),(28,28,1),(29,29,1),(30,30,1),(31,31,1),(32,32,1),(33,33,1),(34,34,1),(35,35,1),(36,36,1),(37,37,1),(38,38,1),(39,39,1),(40,40,1),(41,41,1),(42,42,1),(43,43,1),(44,44,1),(45,45,1),(46,46,1),(47,47,1),(48,48,1),(49,49,1),(50,50,1),(51,51,1),(52,52,1),(53,53,1),(54,54,1),(55,55,1),(56,56,1),(57,57,1),(58,58,1),(59,59,1),(60,60,1),(61,61,1),(62,62,1),(63,63,1),(64,64,1),(65,65,1),(66,66,1),(67,67,1),(68,68,1),(69,69,1),(70,70,1),(71,71,1),(72,72,1),(73,73,1),(74,74,1),(75,75,1),(76,76,1),(77,77,1),(78,78,1),(79,79,1),(80,80,1),(81,81,1),(82,82,1),(83,83,1),(84,84,1),(85,85,1),(86,86,1),(87,87,1),(88,88,1),(89,89,1),(90,90,1),(91,91,1),(92,92,1),(93,93,1),(94,94,1),(95,95,1),(96,96,1),(97,97,1),(98,98,1),(99,99,1),(100,100,1),(101,1,2),(102,2,2),(103,3,2),(104,4,2),(105,5,2),(106,6,2),(107,7,2),(108,8,2),(109,9,2),(110,10,2),(111,11,2),(112,12,2),(113,13,2),(114,14,2),(115,15,2),(116,16,2),(117,17,2),(118,18,2),(119,19,2),(120,20,2),(121,21,2),(122,22,2),(123,23,2),(124,24,2),(125,25,2),(126,26,2),(127,27,2),(128,28,2),(129,29,2),(130,30,2),(131,31,2),(132,32,2),(133,33,2),(134,34,2),(135,35,2),(136,36,2),(137,37,2),(138,38,2),(139,39,2),(140,40,2),(141,41,2),(142,42,2),(143,43,2),(144,44,2),(145,45,2),(146,46,2),(147,47,2),(148,48,2),(149,49,2),(150,50,2),(151,51,2),(152,52,2),(153,53,2),(154,54,2),(155,55,2),(156,56,2),(157,57,2),(158,58,2),(159,59,2),(160,60,2),(161,61,2),(162,62,2),(163,63,2),(164,64,2),(165,65,2),(166,66,2),(167,67,2),(168,68,2),(169,69,2),(170,70,2),(171,71,2),(172,72,2),(173,73,2),(174,74,2),(175,75,2),(176,76,2),(177,77,2),(178,78,2),(179,79,2),(180,80,2),(181,81,2),(182,82,2),(183,83,2),(184,84,2),(185,85,2),(186,86,2),(187,87,2),(188,88,2),(189,89,2),(190,90,2),(191,91,2),(192,92,2),(193,93,2),(194,94,2),(195,95,2),(196,96,2),(197,97,2),(198,98,2),(199,99,2),(200,100,2),(201,1,3),(202,2,3),(203,3,3),(204,4,3),(205,5,3),(206,6,3),(207,7,3),(208,8,3),(209,9,3),(210,10,3),(211,11,3),(212,12,3),(213,13,3),(214,14,3),(215,15,3),(216,16,3),(217,17,3),(218,18,3),(219,19,3),(220,20,3),(221,21,3),(222,22,3),(223,23,3),(224,24,3),(225,25,3),(226,26,3),(227,27,3),(228,28,3),(229,29,3),(230,30,3),(231,31,3),(232,32,3),(233,33,3),(234,34,3),(235,35,3),(236,36,3),(237,37,3),(238,38,3),(239,39,3),(240,40,3),(241,41,3),(242,42,3),(243,43,3),(244,44,3),(245,45,3),(246,46,3),(247,47,3),(248,48,3),(249,49,3),(250,50,3),(251,51,3),(252,52,3),(253,53,3),(254,54,3),(255,55,3),(256,56,3),(257,57,3),(258,58,3),(259,59,3),(260,60,3),(261,61,3),(262,62,3),(263,63,3),(264,64,3),(265,65,3),(266,66,3),(267,67,3),(268,68,3),(269,69,3),(270,70,3),(271,71,3),(272,72,3),(273,73,3),(274,74,3),(275,75,3),(276,76,3),(277,77,3),(278,78,3),(279,79,3),(280,80,3),(281,81,3),(282,82,3),(283,83,3),(284,84,3),(285,85,3),(286,86,3),(287,87,3),(288,88,3),(289,89,3),(290,90,3),(291,91,3),(292,92,3),(293,93,3),(294,94,3),(295,95,3),(296,96,3),(297,97,3),(298,98,3),(299,99,3),(300,100,3);
/*!40000 ALTER TABLE `asientos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `entrada`
--

DROP TABLE IF EXISTS `entrada`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `entrada` (
  `id_entrada` int NOT NULL AUTO_INCREMENT,
  `funcion_id_funcion` int NOT NULL,
  `usuarios_id_usuarios` int NOT NULL,
  `asiento_id_asiento` int NOT NULL,
  `precio` float NOT NULL,
  PRIMARY KEY (`id_entrada`),
  KEY `fk_entrada_funcion1_idx` (`funcion_id_funcion`),
  KEY `fk_entrada_usuarios1_idx` (`usuarios_id_usuarios`),
  KEY `fk_entrada_asiento1_idx` (`asiento_id_asiento`),
  CONSTRAINT `fk_entrada_asiento1` FOREIGN KEY (`asiento_id_asiento`) REFERENCES `asientos` (`id_asiento`),
  CONSTRAINT `fk_entrada_funcion1` FOREIGN KEY (`funcion_id_funcion`) REFERENCES `funcion` (`id_funcion`),
  CONSTRAINT `fk_entrada_usuarios1` FOREIGN KEY (`usuarios_id_usuarios`) REFERENCES `usuarios` (`id_usuarios`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `entrada`
--

LOCK TABLES `entrada` WRITE;
/*!40000 ALTER TABLE `entrada` DISABLE KEYS */;
/*!40000 ALTER TABLE `entrada` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `funcion`
--

DROP TABLE IF EXISTS `funcion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `funcion` (
  `id_funcion` int NOT NULL AUTO_INCREMENT,
  `horario` datetime NOT NULL,
  `sala_id_sala` int NOT NULL,
  `peliculas_id_peliculas` int NOT NULL,
  PRIMARY KEY (`id_funcion`),
  KEY `fk_entrada_sala_idx` (`sala_id_sala`),
  KEY `fk_entrada_peliculas1_idx` (`peliculas_id_peliculas`),
  CONSTRAINT `fk_entrada_peliculas1` FOREIGN KEY (`peliculas_id_peliculas`) REFERENCES `peliculas` (`id_peliculas`),
  CONSTRAINT `fk_entrada_sala` FOREIGN KEY (`sala_id_sala`) REFERENCES `sala` (`id_sala`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funcion`
--

LOCK TABLES `funcion` WRITE;
/*!40000 ALTER TABLE `funcion` DISABLE KEYS */;
/*!40000 ALTER TABLE `funcion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `generos`
--

DROP TABLE IF EXISTS `generos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `generos` (
  `id_generos` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  PRIMARY KEY (`id_generos`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `generos`
--

LOCK TABLES `generos` WRITE;
/*!40000 ALTER TABLE `generos` DISABLE KEYS */;
INSERT INTO `generos` VALUES (1,'Comedia'),(2,'Accion'),(3,'Aventura'),(4,'Terror'),(5,'Ciencia Ficcion'),(6,'Musical'),(7,'Drama'),(8,'Suspenso');
/*!40000 ALTER TABLE `generos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `peliculas`
--

DROP TABLE IF EXISTS `peliculas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `peliculas` (
  `id_peliculas` int NOT NULL AUTO_INCREMENT,
  `titulo` varchar(45) NOT NULL,
  `resenia` varchar(150) NOT NULL,
  `duracion` int NOT NULL,
  `calificacion` varchar(45) NOT NULL,
  `idioma` tinyint(1) NOT NULL,
  `generos_id_generos` int NOT NULL,
  `imagen_link` varchar(250) NOT NULL,
  PRIMARY KEY (`id_peliculas`),
  KEY `fk_peliculas_generos1_idx` (`generos_id_generos`),
  CONSTRAINT `fk_peliculas_generos1` FOREIGN KEY (`generos_id_generos`) REFERENCES `generos` (`id_generos`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `peliculas`
--

LOCK TABLES `peliculas` WRITE;
/*!40000 ALTER TABLE `peliculas` DISABLE KEYS */;
/*!40000 ALTER TABLE `peliculas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sala`
--

DROP TABLE IF EXISTS `sala`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sala` (
  `id_sala` int NOT NULL AUTO_INCREMENT,
  `capacidad` int NOT NULL,
  PRIMARY KEY (`id_sala`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sala`
--

LOCK TABLES `sala` WRITE;
/*!40000 ALTER TABLE `sala` DISABLE KEYS */;
INSERT INTO `sala` VALUES (1,100),(2,100),(3,100);
/*!40000 ALTER TABLE `sala` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id_usuarios` int NOT NULL AUTO_INCREMENT,
  `email` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `usuario` varchar(45) NOT NULL,
  `fecha_nacimiento` datetime NOT NULL,
  PRIMARY KEY (`id_usuarios`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-20 23:56:38
