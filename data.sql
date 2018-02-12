-- MySQL dump 10.13  Distrib 5.5.54, for debian-linux-gnu (x86_64)
--
-- Host: iglesiabetel.mysql.pythonanywhere-services.com    Database: iglesiabetel$default
-- ------------------------------------------------------
-- Server version	5.6.27-log

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
-- Table structure for table `accounts_users`
--

DROP TABLE IF EXISTS `accounts_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_users` (
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `ci` varchar(60) NOT NULL,
  `username` varchar(40) DEFAULT NULL,
  `email` varchar(254) NOT NULL,
  `first_name` varchar(40) NOT NULL,
  `last_name` varchar(40) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `is_alumno` tinyint(1) NOT NULL,
  `is_profesor` tinyint(1) NOT NULL,
  `is_inscripcion` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`ci`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_users`
--

LOCK TABLES `accounts_users` WRITE;
/*!40000 ALTER TABLE `accounts_users` DISABLE KEYS */;
INSERT INTO `accounts_users` VALUES ('pbkdf2_sha256$36000$gFr860D9Uh2Z$b4FuyiEXEVQbs3pXJREh7UNzWoO5Wxw5G8KUbDlxPPA=','2018-02-09 00:33:34.821292','123456789','123456789','HJDBS@GMAIL.Com','DSHB','DJSBDSJ',1,1,0,0,0,1,'2018-01-01 01:35:41.216796','2018-01-01 01:35:41.300781','2018-01-01 01:35:41.301757'),('pbkdf2_sha256$36000$pcjyzkCZpxDY$eVdIW9GNRmTpP0swy0yZ2GM4TeoGrLOXbqawKCRp3GE=','2018-02-09 01:14:03.946325','25506161','25506161','DNJSDSDS@GMAIL.COM','FRANCELYS','GIL',1,0,0,0,1,0,'2018-02-09 00:25:09.437882','2018-02-09 00:25:09.505300','2018-02-09 00:25:09.505326'),('pbkdf2_sha256$36000$OWCcucADYffe$Ae9sZhKqCo1vZfFWdv+P4SLINwAOQ/GyDyFhTJ1u03k=','2018-02-10 12:31:23.875269','26503305','26503305','DSBDH@GMAIL.COM','HDSUHDSU','DSDBHJ',1,1,1,1,1,0,'2018-01-01 01:15:12.199218','2018-01-01 01:15:12.395507','2018-01-01 01:15:12.395507'),('pbkdf2_sha256$36000$dwrIHm10LT0q$O86Zd3HPpi/OENrB/15/2nB6pVs7a2JLMp3jzijdCyA=','2018-02-09 00:35:05.061230','27277934','27277934','DSD@GMAIL.COM','WILERSY','HIDALGO',1,1,0,1,0,0,'2018-02-09 00:34:38.242882','2018-02-09 00:34:38.405937','2018-02-09 00:34:38.405964'),('pbkdf2_sha256$36000$wOsj1NcBBEXG$WlfhzI8qTmAdXOnYjmB8s4Y3vJpabfuG+Ip5boLQACw=','2018-02-09 00:50:21.681522','5128468','5128468','PAPA@GMAIL.COM','PAPA','PAPA',1,0,0,0,1,0,'2018-02-09 00:49:58.421374','2018-02-09 00:49:58.521019','2018-02-09 00:49:58.521075');
/*!40000 ALTER TABLE `accounts_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_users_groups`
--

DROP TABLE IF EXISTS `accounts_users_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_users_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `users_id` varchar(60) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `accounts_users_groups_users_id_group_id_8dfb39d5_uniq` (`users_id`,`group_id`),
  KEY `accounts_users_groups_group_id_371be490_fk_auth_group_id` (`group_id`),
  CONSTRAINT `accounts_users_groups_group_id_371be490_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `accounts_users_groups_users_id_c8303f87_fk_accounts_users_ci` FOREIGN KEY (`users_id`) REFERENCES `accounts_users` (`ci`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_users_groups`
--

LOCK TABLES `accounts_users_groups` WRITE;
/*!40000 ALTER TABLE `accounts_users_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_users_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_users_user_permissions`
--

DROP TABLE IF EXISTS `accounts_users_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_users_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `users_id` varchar(60) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `accounts_users_user_perm_users_id_permission_id_866b235f_uniq` (`users_id`,`permission_id`),
  KEY `accounts_users_user__permission_id_5f3d0fff_fk_auth_perm` (`permission_id`),
  CONSTRAINT `accounts_users_user__permission_id_5f3d0fff_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `accounts_users_user__users_id_62a47b5b_fk_accounts_` FOREIGN KEY (`users_id`) REFERENCES `accounts_users` (`ci`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_users_user_permissions`
--

LOCK TABLES `accounts_users_user_permissions` WRITE;
/*!40000 ALTER TABLE `accounts_users_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_users_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add asigna_ materia',6,'add_asigna_materia'),(17,'Can change asigna_ materia',6,'change_asigna_materia'),(18,'Can delete asigna_ materia',6,'delete_asigna_materia'),(19,'Can add inscripcion',7,'add_inscripcion'),(20,'Can change inscripcion',7,'change_inscripcion'),(21,'Can delete inscripcion',7,'delete_inscripcion'),(22,'Can add materia',8,'add_materia'),(23,'Can change materia',8,'change_materia'),(24,'Can delete materia',8,'delete_materia'),(25,'Can add nivel',9,'add_nivel'),(26,'Can change nivel',9,'change_nivel'),(27,'Can delete nivel',9,'delete_nivel'),(28,'Can add notas',10,'add_notas'),(29,'Can change notas',10,'change_notas'),(30,'Can delete notas',10,'delete_notas'),(31,'Can add notificacion',11,'add_notificacion'),(32,'Can change notificacion',11,'change_notificacion'),(33,'Can delete notificacion',11,'delete_notificacion'),(34,'Can add persona',12,'add_persona'),(35,'Can change persona',12,'change_persona'),(36,'Can delete persona',12,'delete_persona'),(37,'Can add profesor',13,'add_profesor'),(38,'Can change profesor',13,'change_profesor'),(39,'Can delete profesor',13,'delete_profesor'),(40,'Can add users',14,'add_users'),(41,'Can change users',14,'change_users'),(42,'Can delete users',14,'delete_users');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `datos_asigna_materia`
--

DROP TABLE IF EXISTS `datos_asigna_materia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `datos_asigna_materia` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `materia_id` int(11) NOT NULL,
  `profesor_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `materia_id` (`materia_id`),
  UNIQUE KEY `profesor_id` (`profesor_id`),
  CONSTRAINT `datos_asigna_materia_materia_id_53ab8dc3_fk_datos_mat` FOREIGN KEY (`materia_id`) REFERENCES `datos_materia` (`id_materia`),
  CONSTRAINT `datos_asigna_materia_profesor_id_f9506881_fk_datos_pro` FOREIGN KEY (`profesor_id`) REFERENCES `datos_profesor` (`cedula_profesor`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `datos_asigna_materia`
--

LOCK TABLES `datos_asigna_materia` WRITE;
/*!40000 ALTER TABLE `datos_asigna_materia` DISABLE KEYS */;
INSERT INTO `datos_asigna_materia` VALUES (1,1,25506161),(2,2,5128468);
/*!40000 ALTER TABLE `datos_asigna_materia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `datos_inscripcion`
--

DROP TABLE IF EXISTS `datos_inscripcion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `datos_inscripcion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lapso_ano` date NOT NULL,
  `estatus` varchar(20) NOT NULL,
  `cedula_id` int(11) NOT NULL,
  `id_nivel_id` int(11) NOT NULL,
  `terminado` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `datos_inscripcion_cedula_id_3f2a2331_fk_datos_persona_cedula` (`cedula_id`),
  KEY `datos_inscripcion_id_nivel_id_ecb5da26_fk_datos_nivel_id_nivel` (`id_nivel_id`),
  CONSTRAINT `datos_inscripcion_cedula_id_3f2a2331_fk_datos_persona_cedula` FOREIGN KEY (`cedula_id`) REFERENCES `datos_persona` (`cedula`),
  CONSTRAINT `datos_inscripcion_id_nivel_id_ecb5da26_fk_datos_nivel_id_nivel` FOREIGN KEY (`id_nivel_id`) REFERENCES `datos_nivel` (`id_nivel`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `datos_inscripcion`
--

LOCK TABLES `datos_inscripcion` WRITE;
/*!40000 ALTER TABLE `datos_inscripcion` DISABLE KEYS */;
INSERT INTO `datos_inscripcion` VALUES (1,'2018-02-08','1',27277934,1,0);
/*!40000 ALTER TABLE `datos_inscripcion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `datos_materia`
--

DROP TABLE IF EXISTS `datos_materia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `datos_materia` (
  `id_materia` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_materia` varchar(40) NOT NULL,
  `id_nivel_id` int(11) NOT NULL,
  PRIMARY KEY (`id_materia`),
  KEY `datos_materia_id_nivel_id_9de5eb5b_fk_datos_nivel_id_nivel` (`id_nivel_id`),
  CONSTRAINT `datos_materia_id_nivel_id_9de5eb5b_fk_datos_nivel_id_nivel` FOREIGN KEY (`id_nivel_id`) REFERENCES `datos_nivel` (`id_nivel`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `datos_materia`
--

LOCK TABLES `datos_materia` WRITE;
/*!40000 ALTER TABLE `datos_materia` DISABLE KEYS */;
INSERT INTO `datos_materia` VALUES (1,'Fundamento',1),(2,'Familia',1),(3,'Interseción',2),(4,'Vision',2),(5,'Consolidación',3),(6,'Consolidación',3);
/*!40000 ALTER TABLE `datos_materia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `datos_nivel`
--

DROP TABLE IF EXISTS `datos_nivel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `datos_nivel` (
  `id_nivel` int(11) NOT NULL AUTO_INCREMENT,
  `nivel` varchar(10) NOT NULL,
  PRIMARY KEY (`id_nivel`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `datos_nivel`
--

LOCK TABLES `datos_nivel` WRITE;
/*!40000 ALTER TABLE `datos_nivel` DISABLE KEYS */;
INSERT INTO `datos_nivel` VALUES (1,'I'),(2,'II'),(3,'III');
/*!40000 ALTER TABLE `datos_nivel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `datos_notas`
--

DROP TABLE IF EXISTS `datos_notas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `datos_notas` (
  `id_nota` int(11) NOT NULL AUTO_INCREMENT,
  `nota_persona` varchar(20) NOT NULL,
  `cedula_id` int(11) NOT NULL,
  `id_materia_id` int(11) NOT NULL,
  PRIMARY KEY (`id_nota`),
  KEY `datos_notas_cedula_id_d3c81ad9_fk_datos_inscripcion_id` (`cedula_id`),
  KEY `datos_notas_id_materia_id_9b322e7e_fk_datos_materia_id_materia` (`id_materia_id`),
  CONSTRAINT `datos_notas_cedula_id_d3c81ad9_fk_datos_inscripcion_id` FOREIGN KEY (`cedula_id`) REFERENCES `datos_inscripcion` (`id`),
  CONSTRAINT `datos_notas_id_materia_id_9b322e7e_fk_datos_materia_id_materia` FOREIGN KEY (`id_materia_id`) REFERENCES `datos_materia` (`id_materia`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `datos_notas`
--

LOCK TABLES `datos_notas` WRITE;
/*!40000 ALTER TABLE `datos_notas` DISABLE KEYS */;
INSERT INTO `datos_notas` VALUES (1,'1',1,1);
/*!40000 ALTER TABLE `datos_notas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `datos_notificacion`
--

DROP TABLE IF EXISTS `datos_notificacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `datos_notificacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(20) NOT NULL,
  `descripcion` varchar(80) NOT NULL,
  `hora` datetime(6) NOT NULL,
  `estatus` tinyint(1) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `datos_notificacion_user_id_dce28347_fk_datos_persona_cedula` (`user_id`),
  CONSTRAINT `datos_notificacion_user_id_dce28347_fk_datos_persona_cedula` FOREIGN KEY (`user_id`) REFERENCES `datos_persona` (`cedula`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `datos_notificacion`
--

LOCK TABLES `datos_notificacion` WRITE;
/*!40000 ALTER TABLE `datos_notificacion` DISABLE KEYS */;
INSERT INTO `datos_notificacion` VALUES (1,'Carga de nota','Se le ha cargado una nueva nota','2018-02-09 00:40:39.009237',0,27277934);
/*!40000 ALTER TABLE `datos_notificacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `datos_persona`
--

DROP TABLE IF EXISTS `datos_persona`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `datos_persona` (
  `cedula` int(11) NOT NULL,
  `nombre` varchar(60) NOT NULL,
  `apellido` varchar(60) NOT NULL,
  `fecha_de_nacimiento` date NOT NULL,
  `sexo` varchar(15) NOT NULL,
  `direccion` varchar(60) NOT NULL,
  `telefono_residencial` varchar(14) NOT NULL,
  `celular_number` varchar(20) NOT NULL,
  `celular` varchar(20) NOT NULL,
  `email` varchar(254) NOT NULL,
  `estado_civil` varchar(15) NOT NULL,
  `trabaja` varchar(10) NOT NULL,
  `profesion` varchar(60) NOT NULL,
  `estudio_ori` varchar(60) NOT NULL,
  `ing_famil` int(11) NOT NULL,
  `iglesia` varchar(60) NOT NULL,
  `pastor` varchar(25) NOT NULL,
  `estudio_teo` varchar(20) NOT NULL,
  `instituto` varchar(60) DEFAULT NULL,
  `titulo_obte` varchar(25) DEFAULT NULL,
  `actividad` varchar(60) NOT NULL,
  `ministerio` varchar(60) NOT NULL,
  `razon` varchar(60) NOT NULL,
  `user_id` varchar(60) NOT NULL,
  PRIMARY KEY (`cedula`),
  KEY `datos_persona_user_id_49dee89f_fk_accounts_users_ci` (`user_id`),
  CONSTRAINT `datos_persona_user_id_49dee89f_fk_accounts_users_ci` FOREIGN KEY (`user_id`) REFERENCES `accounts_users` (`ci`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `datos_persona`
--

LOCK TABLES `datos_persona` WRITE;
/*!40000 ALTER TABLE `datos_persona` DISABLE KEYS */;
INSERT INTO `datos_persona` VALUES (27277934,'WILERSY','HIDALGO','1998-05-01','Masculino','DSKMNDSKNDSKJNDSJK','','','','DSD@GMAIL.COM','Soltero','si','DNSJKNDSJKN','JKDNSJKNDJSK',433434,'DJKSNDJKSNDJSK','DJKSNJDKNKJ','si','DSDNSJKDNSKJ','DJNSJKDNJSK','JKDSNDKJNSJKDNSJDKNSJKDN','Consolidacion','DKLSMDKLSMDLKSD','27277934');
/*!40000 ALTER TABLE `datos_persona` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `datos_profesor`
--

DROP TABLE IF EXISTS `datos_profesor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `datos_profesor` (
  `cedula_profesor` int(11) NOT NULL,
  `nombre_profesor` varchar(20) NOT NULL,
  `apellido_profesor` varchar(20) NOT NULL,
  `telefono_profesor` varchar(11) NOT NULL,
  `email_profesor` varchar(254) NOT NULL,
  `estatus` tinyint(1) DEFAULT NULL,
  `user_id` varchar(60) NOT NULL,
  PRIMARY KEY (`cedula_profesor`),
  KEY `datos_profesor_user_id_b9ed01cf_fk_accounts_users_ci` (`user_id`),
  CONSTRAINT `datos_profesor_user_id_b9ed01cf_fk_accounts_users_ci` FOREIGN KEY (`user_id`) REFERENCES `accounts_users` (`ci`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `datos_profesor`
--

LOCK TABLES `datos_profesor` WRITE;
/*!40000 ALTER TABLE `datos_profesor` DISABLE KEYS */;
INSERT INTO `datos_profesor` VALUES (5128468,'PAPA','PAPA','3232323','PAPA@GMAIL.COM',1,'5128468'),(25506161,'FRANCELYS','GIL','02572510432','DNJSDSDS@GMAIL.COM',1,'25506161');
/*!40000 ALTER TABLE `datos_profesor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_accounts_users_ci` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_accounts_users_ci` FOREIGN KEY (`user_id`) REFERENCES `accounts_users` (`ci`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2018-02-09 00:21:09.773260','00098390','00098390, DJSBDBSJH, BDHBSJBDJH',3,'',14,'26503305'),(2,'2018-02-09 00:21:09.781015','01051994','01051994, DJSBDBSJH, BDHBSJBDJH',3,'',14,'26503305'),(3,'2018-02-09 00:21:09.791245','01051998','01051998, DJSBDBSJH, BDHBSJBDJH',3,'',14,'26503305'),(4,'2018-02-09 00:21:09.799205','12121212','12121212, SJDNJKN, KSDNKJDSNKJDN',3,'',14,'26503305'),(5,'2018-02-09 00:21:09.806996','1234','1234, DBSBHJ, HJBSDHDJHJ',3,'',14,'26503305'),(6,'2018-02-09 00:21:09.814900','123456789','123456789, DSHB, DJSBDSJ',3,'',14,'26503305'),(7,'2018-02-09 00:21:09.823121','12345785','12345785, AURA, CASTIILO',3,'',14,'26503305'),(8,'2018-02-09 00:21:09.833907','13039155','13039155, PAPA, DJSBDHJ',3,'',14,'26503305'),(9,'2018-02-09 00:21:09.841692','15799191','15799191, HUMBERLYS, SDJKSNDKJNSKJ',3,'',14,'26503305'),(10,'2018-02-09 00:21:09.849460','21190411','21190411, DSB, BSDJDBS',3,'',14,'26503305'),(11,'2018-02-09 00:21:09.857273','23239789','23239789, HUMNBER, JDKSNDJKN',3,'',14,'26503305'),(12,'2018-02-09 00:21:09.865136','25424711','25424711, GABY, JSBDHJ',3,'',14,'26503305'),(13,'2018-02-09 00:21:09.873117','25506616','25506616, FRANCEUS, SBJD',3,'',14,'26503305'),(14,'2018-02-09 00:21:09.881069','26188539','26188539, HUMBERLYS, COLMENAREZ',3,'',14,'26503305'),(15,'2018-02-09 00:21:09.889071','27277934','27277934, DJSBDBhj, SBDHJD',3,'',14,'26503305'),(16,'2018-02-09 00:21:09.896880','27277935','27277935, PERSONA NUEVA, NUEVA PERSONA',3,'',14,'26503305'),(17,'2018-02-09 00:21:09.905968','3232323','3232323, DSDNSJKDNJKN, JKNDSJKDNSJKDN',3,'',14,'26503305'),(18,'2018-02-09 00:21:09.913532','38974837','38974837, DJSBDBSJH, BDHBSJBDJH',3,'',14,'26503305'),(19,'2018-02-09 00:21:09.921169','43437643','43437643, JKDNSKJNDJSKN, KJDNJSKNDJKSN',3,'',14,'26503305'),(20,'2018-02-09 00:21:09.929042','43849444','43849444, FJKDNFJKn, DNSJKNDKJ',3,'',14,'26503305'),(21,'2018-02-09 00:21:09.936676','47637846','47637846, DJSBDBSJH, BDHBSJBDJH',3,'',14,'26503305'),(22,'2018-02-09 00:21:09.944231','47836473','47836473, DJSBDBSJH, BDHBSJBDJH',3,'',14,'26503305'),(23,'2018-02-09 00:21:09.951888','47893483','47893483, DSNKJDNSJKDN, DNSNDKJS',3,'',14,'26503305'),(24,'2018-02-09 00:21:09.959790','5128468','5128468, SBDH, HJBJDHJBSDHJ',3,'',14,'26503305'),(25,'2018-02-09 00:21:09.966980','545645757','545645757, DSJDBSDHSHj, BDJSDhj',3,'',14,'26503305'),(26,'2018-02-09 00:21:09.974186','64876378','64876378, NJDKNSKJDNSKJ, JKDNSJKDNSJKND',3,'',14,'26503305'),(27,'2018-02-09 00:21:09.982591','68367486','68367486, PROFE NUEVO, PROFE NUEVO',3,'',14,'26503305'),(28,'2018-02-09 00:21:09.989764','73232326','73232326, HUMBERU, JDSNJDSNJDKN',3,'',14,'26503305'),(29,'2018-02-09 00:21:09.997173','74637864','74637864, DSJBDBSDJH, JD SBDBJH',3,'',14,'26503305'),(30,'2018-02-09 00:21:10.006241','74863746','74863746, DJSBDBSJH, BDHBSJBDJH',3,'',14,'26503305'),(31,'2018-02-09 00:21:10.013686','75677657','75677657, DJSBDBSJH, BDHBSJBDJH',3,'',14,'26503305'),(32,'2018-02-09 00:21:10.020933','76473864','76473864, JDNSJKNDJSKN, DJKSNKJDNSJK',3,'',14,'26503305'),(33,'2018-02-09 00:21:10.028799','78364738','78364738, DJSBDBSJH, BDHBSJBDJH',3,'',14,'26503305'),(34,'2018-02-09 00:21:10.037548','78643876','78643876, DJSBDBSJH, BDHBSJBDJH',3,'',14,'26503305'),(35,'2018-02-09 00:21:10.045030','8064775','8064775, DJKSBNDKNSjk, NJKNSDJKDNSJK',3,'',14,'26503305'),(36,'2018-02-09 00:21:10.054993','86868765','86868765, PROFESIR, PROFESOR',3,'',14,'26503305'),(37,'2018-02-09 00:21:10.063424','87389473','87389473, JDSKNDJSKND, JDNSJKNDJKN',3,'',14,'26503305'),(38,'2018-02-09 00:21:10.071402','89473897','89473897, KDSKLDNMSLKMD, MDLKSMDLKMSLK',3,'',14,'26503305'),(39,'2018-02-09 00:21:10.079102','89479837','89479837, DJSBDBSJH, BDHBSJBDJH',3,'',14,'26503305'),(40,'2018-02-09 00:21:10.086312','89743897','89743897, JKDNSJKNDSJKn, JKDNSJKDNSKJND',3,'',14,'26503305'),(41,'2018-02-09 00:21:10.093378','89754975','89754975, DJSBDBSJH, BDHBSJBDJH',3,'',14,'26503305'),(42,'2018-02-09 00:21:54.524627','1','I',1,'[{\"added\": {}}]',9,'26503305'),(43,'2018-02-09 00:22:02.851026','2','II',1,'[{\"added\": {}}]',9,'26503305'),(44,'2018-02-09 00:22:09.501704','3','III',1,'[{\"added\": {}}]',9,'26503305'),(45,'2018-02-09 00:22:36.953614','1','Fundamento, I',1,'[{\"added\": {}}]',8,'26503305'),(46,'2018-02-09 00:22:44.479317','2','Familia, I',1,'[{\"added\": {}}]',8,'26503305'),(47,'2018-02-09 00:22:50.646850','3','Interseción, II',1,'[{\"added\": {}}]',8,'26503305'),(48,'2018-02-09 00:23:06.484331','4','Vision, II',1,'[{\"added\": {}}]',8,'26503305'),(49,'2018-02-09 00:23:14.690176','5','Consolidación, III',1,'[{\"added\": {}}]',8,'26503305'),(50,'2018-02-09 00:23:24.225192','6','Consolidación, III',1,'[{\"added\": {}}]',8,'26503305');
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (14,'accounts','users'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(6,'datos','asigna_materia'),(7,'datos','inscripcion'),(8,'datos','materia'),(9,'datos','nivel'),(10,'datos','notas'),(11,'datos','notificacion'),(12,'datos','persona'),(13,'datos','profesor'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-02-09 00:00:13.174776'),(2,'contenttypes','0002_remove_content_type_name','2018-02-09 00:00:13.330211'),(3,'auth','0001_initial','2018-02-09 00:00:13.982568'),(4,'auth','0002_alter_permission_name_max_length','2018-02-09 00:00:14.054322'),(5,'auth','0003_alter_user_email_max_length','2018-02-09 00:00:14.070706'),(6,'auth','0004_alter_user_username_opts','2018-02-09 00:00:14.086743'),(7,'auth','0005_alter_user_last_login_null','2018-02-09 00:00:14.102824'),(8,'auth','0006_require_contenttypes_0002','2018-02-09 00:00:14.112550'),(9,'auth','0007_alter_validators_add_error_messages','2018-02-09 00:00:14.127682'),(10,'auth','0008_alter_user_username_max_length','2018-02-09 00:00:14.145987'),(11,'accounts','0001_initial','2018-02-09 00:00:15.155328'),(12,'admin','0001_initial','2018-02-09 00:00:15.550772'),(13,'admin','0002_logentry_remove_auto_add','2018-02-09 00:00:15.588701'),(14,'datos','0001_initial','2018-02-09 00:00:18.334216'),(15,'datos','0002_auto_20180207_2254','2018-02-09 00:00:18.505835'),(16,'datos','0003_auto_20180207_2256','2018-02-09 00:00:18.551907'),(17,'datos','0004_auto_20180208_0904','2018-02-09 00:00:18.698226'),(18,'sessions','0001_initial','2018-02-09 00:00:18.842255');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('4gzatg9z9dpjznj2dz4fm6958vw7hqbk','OTkzZDcxNDFlOGI2MTQ5NDMzMTMyNWUyYWRmMzhmNWMxNTk5NGIxNTp7Il9hdXRoX3VzZXJfaWQiOiIyNjUwMzMwNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMmU2OWJhOTNmMmNmYzRkMjE0ZDJkNzFlZjQ4YzM0YzIzM2UzMzUxNyJ9','2018-02-09 00:58:10.399734'),('67kc976gjfrikafth3103r6eximdxo7k','OTkzZDcxNDFlOGI2MTQ5NDMzMTMyNWUyYWRmMzhmNWMxNTk5NGIxNTp7Il9hdXRoX3VzZXJfaWQiOiIyNjUwMzMwNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMmU2OWJhOTNmMmNmYzRkMjE0ZDJkNzFlZjQ4YzM0YzIzM2UzMzUxNyJ9','2018-02-09 00:43:39.630045'),('cm9ym8z37ot2vhvexw2n9vzn9wuhvpiv','OTkzZDcxNDFlOGI2MTQ5NDMzMTMyNWUyYWRmMzhmNWMxNTk5NGIxNTp7Il9hdXRoX3VzZXJfaWQiOiIyNjUwMzMwNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMmU2OWJhOTNmMmNmYzRkMjE0ZDJkNzFlZjQ4YzM0YzIzM2UzMzUxNyJ9','2018-02-09 01:02:55.082984'),('ge1igapfi5pbef6zpv14mw5qx7093i7n','N2Q1MjUxOTlmZmMxMTQ4ODc1YzRmNTcxNWRlMDljOWUzMmM5ODE2ZDp7Il9hdXRoX3VzZXJfaWQiOiIyNTUwNjE2MSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZmQyZWJiYzQ4YTNjOGI3ZjVlYzdiYmVhZTIwZjY5OWUxOTI0OGY0MCJ9','2018-02-09 00:42:40.075580'),('gpj0y2nv8ytzbuwna68e74igynfg1rvb','N2Q1MjUxOTlmZmMxMTQ4ODc1YzRmNTcxNWRlMDljOWUzMmM5ODE2ZDp7Il9hdXRoX3VzZXJfaWQiOiIyNTUwNjE2MSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZmQyZWJiYzQ4YTNjOGI3ZjVlYzdiYmVhZTIwZjY5OWUxOTI0OGY0MCJ9','2018-02-09 01:16:05.661268'),('pw2usu7qvl4t7fy3wpz2l9ugmgsptttc','OTkzZDcxNDFlOGI2MTQ5NDMzMTMyNWUyYWRmMzhmNWMxNTk5NGIxNTp7Il9hdXRoX3VzZXJfaWQiOiIyNjUwMzMwNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMmU2OWJhOTNmMmNmYzRkMjE0ZDJkNzFlZjQ4YzM0YzIzM2UzMzUxNyJ9','2018-02-09 00:53:53.647214'),('ryz5w2z6ud5s5wacyk6ormegxs287249','OTkzZDcxNDFlOGI2MTQ5NDMzMTMyNWUyYWRmMzhmNWMxNTk5NGIxNTp7Il9hdXRoX3VzZXJfaWQiOiIyNjUwMzMwNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMmU2OWJhOTNmMmNmYzRkMjE0ZDJkNzFlZjQ4YzM0YzIzM2UzMzUxNyJ9','2018-02-09 01:07:18.866984'),('vimimz04psjj3g6u66drbe1ihcpoyxuv','OTkzZDcxNDFlOGI2MTQ5NDMzMTMyNWUyYWRmMzhmNWMxNTk5NGIxNTp7Il9hdXRoX3VzZXJfaWQiOiIyNjUwMzMwNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMmU2OWJhOTNmMmNmYzRkMjE0ZDJkNzFlZjQ4YzM0YzIzM2UzMzUxNyJ9','2018-02-10 12:34:21.350787'),('yr4mlw1tb9937ixey8cnf8u7fu4xwyww','OTkzZDcxNDFlOGI2MTQ5NDMzMTMyNWUyYWRmMzhmNWMxNTk5NGIxNTp7Il9hdXRoX3VzZXJfaWQiOiIyNjUwMzMwNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMmU2OWJhOTNmMmNmYzRkMjE0ZDJkNzFlZjQ4YzM0YzIzM2UzMzUxNyJ9','2018-02-09 13:10:03.702325');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-02-12 15:02:09
