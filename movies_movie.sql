-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: movies
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `movie`
--

DROP TABLE IF EXISTS `movie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movie` (
  `movie_id` int NOT NULL,
  `release_date` date DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `avg_rating` int DEFAULT NULL,
  PRIMARY KEY (`movie_id`),
  CONSTRAINT `rating` CHECK (((`avg_rating` >= 0) and (`avg_rating` <= 5)))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movie`
--

LOCK TABLES `movie` WRITE;
/*!40000 ALTER TABLE `movie` DISABLE KEYS */;
INSERT INTO `movie` VALUES (1,'2023-05-15','The Shawshank Redemption',2),(2,'1994-09-10','The Godfather',2),(3,'1972-03-24','The Godfather: Part II',1),(4,'1994-07-06','Pulp Fiction',5),(5,'2008-07-18','The Dark Knight',4),(6,'1993-12-15','Schindler\'s List',2),(7,'1999-09-10','Fight Club',2),(8,'1994-06-24','Forrest Gump',4),(9,'1977-05-25','Star Wars: Episode IV - A New Hope',4),(10,'1999-11-10','The Matrix',4),(11,'2023-05-15','The Great Adventure',1),(12,'2022-09-28','Into the Unknown',4),(13,'2023-07-10','City of Dreams',5),(14,'2024-01-03','Lost in Time',4),(15,'2022-11-20','Infinite Horizons',3),(16,'2023-08-12','Echoes of Eternity',4),(17,'2024-03-05','The Last Frontier',4),(18,'2023-02-17','Beyond the Stars',5),(19,'2022-06-30','Journey to Destiny',3),(20,'2023-10-22','A New Beginning',4),(21,'2024-05-18','Endless Possibilities',4),(22,'2023-11-30','The Secret Garden',2),(23,'2022-12-25','Rise of Legends',1),(24,'2024-02-08','Through the Veil',2),(25,'2023-04-14','Above and Beyond',3),(26,'2022-08-05','Under the Moonlight',2),(27,'2024-04-01','The Hidden Path',4),(28,'2023-09-10','Uncharted Waters',2),(29,'2022-10-09','In Pursuit of Happiness',3),(30,'2024-06-20','The Final Countdown',4),(31,'2023-03-02','The Enchanted Forest',2),(32,'2022-07-16','A World Apart',3),(33,'2023-12-08','Above the Clouds',3),(34,'2024-03-19','Into the Abyss',4),(35,'2023-01-11','In the Shadows',3),(36,'2022-05-28','Beyond the Horizon',1),(37,'2023-06-25','Through the Fire',1),(38,'2024-01-30','The Journey Home',2),(39,'2022-11-03','The Road Less Traveled',4),(40,'2023-07-27','The Edge of Tomorrow',4);
/*!40000 ALTER TABLE `movie` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-25 14:49:47
