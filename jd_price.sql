-- MySQL dump 10.13  Distrib 5.7.11, for Win64 (x86_64)
--
-- Host: localhost    Database: jd_price
-- ------------------------------------------------------
-- Server version	5.7.11

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
-- Temporary view structure for view `suit_his_price`
--

DROP TABLE IF EXISTS `suit_his_price`;
/*!50001 DROP VIEW IF EXISTS `suit_his_price`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `suit_his_price` AS SELECT 
 1 AS `id`,
 1 AS `套装`,
 1 AS `类型`,
 1 AS `品名`,
 1 AS `价格`,
 1 AS `时间`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `t_object`
--

DROP TABLE IF EXISTS `t_object`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_object` (
  `tid` bigint(20) NOT NULL AUTO_INCREMENT,
  `jkuid` varchar(20) DEFAULT NULL COMMENT '商品id',
  `obj_name` varchar(100) NOT NULL,
  `type_id` bigint(20) NOT NULL,
  `type_name` varchar(10) NOT NULL,
  PRIMARY KEY (`tid`),
  UNIQUE KEY `t_object_un` (`jkuid`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_object`
--

LOCK TABLES `t_object` WRITE;
/*!40000 ALTER TABLE `t_object` DISABLE KEYS */;
INSERT INTO `t_object` VALUES (21,'2551276','金士顿(Kingston)骇客神条 Fury系列 DDR4 2400 16G 台式机内存',3,'内存'),(22,'689273','九州风神（DEEPCOOL）大霜塔 CPU散热器(多平台/6热管/智能温控/双12CM风扇/附带硅脂/静音)',9,'散热器'),(23,'2249598','美商海盗船（USCorsair）额定550W RM550x 电源（80PLUS金牌/全模组/静音低载风扇停转/十年质保）',4,'电源'),(24,'1748176','英特尔（Intel）酷睿四核 i7-6700k 1151接口 盒装CPU处理器 ',1,'CPU'),(25,'3237242','华硕（ASUS）ROG STRIX-GTX1070-O8G-GAMING 1657-1860MHz 8G/8GHz GDDR5 PCI-E3.0显卡',2,'显卡'),(26,'1791949','技嘉（GIGABYTE）Z170X-Gaming 5主板 (Intel Z170/LGA 1151)',6,'主板'),(27,'3739093','三星(SAMSUNG) 960 PRO 512G M.2 NVMe 固态硬盘',7,'固态'),(29,'2983765','技嘉 GIGABYTE GTX1060 G1 GAMING 1594-1809MHzHz/8008MHz 6G/192bit GDDR5显卡',2,'显卡'),(30,'1760572','华硕（ASUS）Z170-A 主板 （Intel Z170/LGA 1151）',6,'主板'),(31,'746691','东芝(TOSHIBA)3TB 7200转64M SATA3 台式机硬盘(DT01ACA300)',8,'机械'),(32,'840370','安钛克（Antec）额定500W VP500P 电脑电源（主动式PFC/12CM静音风扇/两年质保/双管正激/台式机电源）',4,'电源'),(33,'3317529','乔思伯（JONSBO）U4 银色 ATX机箱 （支持ATX主板/高塔散热器/ATX电源/全铝外壳/5MM厚度钢化玻璃侧板）',5,'机箱'),(34,'2121097','金士顿(Kingston)骇客神条 Fury系列 DDR4 2400 8G 台式机内存',3,'内存'),(35,'1748177','英特尔（Intel）酷睿四核 i5-6600K 1151接口 盒装CPU处理器',1,'CPU'),(37,'3739097','三星(SAMSUNG) 960 EVO 250G M.2 NVMe 固态硬盘',7,'固态'),(38,'3281156','索泰（ZOTAC）Geforce GTX1060-6GD5 X-GAMING OC 1569-1784MHz/8008MHz 6G/192bit GDDR5 PCI-E显卡',2,'显卡'),(39,'1853383','技嘉（GIGABYTE）B150M-D3H主板 (Intel B150/LGA 1151)',6,'主板'),(40,'1540142634','西部数据/WD 西数蓝盘 1TB 64MB7200转1T台式机电脑机械硬盘WD10EZEX',8,'机械'),(42,'3303012','爱国者（aigo）炫影 黑色 分体式水冷机箱（配3把发光风扇/支持ATX主板/钢化玻璃面板/支持背线）',5,'机箱'),(44,'11075508070','英特尔（Intel）酷睿四核 i5-6500 1151接口 盒装CPU处理器',1,'CPU'),(45,'2771147','酷冷至尊(Cooler Master) T400i CPU 散热器(支持INTEL平台/4热管/PWM温控/LED红光风扇/背锁扣具/直触热管)',9,'散热器'),(47,'3528459','索泰（ZOTAC）GeForce GTX1050Ti-4GD5 X-GAMING OC 1354-1468MHz/7008MHz 4G/128bit GDDR5 PCI-E显卡',2,'显卡'),(48,'3775065','微星（MSI）B250M MORTAR主板（Intel B250/LGA 1151）',6,'主板'),(50,'251340','安钛克（Antec）额定450W VP 450P 电脑电源（双显卡接头/两年质保/主动式PFC/12CM静音风扇/台式机电源）',4,'电源'),(52,'1945472','威刚(ADATA)XPG威龙 DDR4 2400 8G台式机内存',3,'内存'),(53,'3701943','英特尔（Intel）酷睿四核I5-7500 盒装CPU处理器',1,'CPU'),(55,'2639360','浦科特 M7VG 256G M.2 2280固态硬盘',7,'固态');
/*!40000 ALTER TABLE `t_object` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_object_history_price`
--

DROP TABLE IF EXISTS `t_object_history_price`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_object_history_price` (
  `tid` bigint(20) NOT NULL AUTO_INCREMENT,
  `price` decimal(10,0) NOT NULL,
  `t_suit_history_id` bigint(20) NOT NULL,
  `gmt_create` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `obj_id` bigint(20) NOT NULL,
  PRIMARY KEY (`tid`)
) ENGINE=InnoDB AUTO_INCREMENT=187 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_object_history_price`
--

LOCK TABLES `t_object_history_price` WRITE;
/*!40000 ALTER TABLE `t_object_history_price` DISABLE KEYS */;
INSERT INTO `t_object_history_price` VALUES (36,969,-1,'2017-03-08 23:36:51',21),(37,219,-1,'2017-03-08 23:36:51',22),(38,799,-1,'2017-03-08 23:36:52',23),(39,2649,-1,'2017-03-08 23:36:52',24),(40,3699,-1,'2017-03-08 23:36:52',25),(41,1499,-1,'2017-03-08 23:36:52',26),(42,2799,-1,'2017-03-08 23:36:52',27),(43,579,-1,'2017-03-08 23:36:52',28),(44,2199,-1,'2017-03-08 23:36:53',29),(45,1199,-1,'2017-03-08 23:36:53',30),(46,579,-1,'2017-03-08 23:36:53',31),(47,299,-1,'2017-03-08 23:36:53',32),(48,399,-1,'2017-03-08 23:36:53',33),(49,479,-1,'2017-03-08 23:36:54',34),(50,1769,-1,'2017-03-08 23:36:54',35),(51,219,-1,'2017-03-08 23:36:54',36),(52,1099,-1,'2017-03-08 23:36:54',37),(53,1999,-1,'2017-03-08 23:36:54',38),(54,599,-1,'2017-03-08 23:36:54',39),(55,328,-1,'2017-03-08 23:36:55',40),(56,259,-1,'2017-03-08 23:36:55',41),(57,219,-1,'2017-03-08 23:36:55',42),(58,419,-1,'2017-03-08 23:36:55',43),(59,1409,-1,'2017-03-08 23:36:55',44),(60,99,-1,'2017-03-08 23:36:55',45),(61,659,-1,'2017-03-08 23:36:56',46),(62,1199,-1,'2017-03-08 23:36:56',47),(63,669,-1,'2017-03-08 23:36:56',48),(64,328,-1,'2017-03-08 23:36:56',49),(65,259,-1,'2017-03-08 23:36:56',50),(66,219,-1,'2017-03-08 23:36:57',51),(67,419,-1,'2017-03-08 23:36:57',52),(68,1579,-1,'2017-03-08 23:36:57',53),(69,99,-1,'2017-03-08 23:36:57',54),(70,659,-1,'2017-03-08 23:36:57',55),(71,969,-1,'2017-03-11 13:36:29',21),(72,219,-1,'2017-03-11 13:36:29',22),(73,799,-1,'2017-03-11 13:36:29',23),(74,2649,-1,'2017-03-11 13:36:29',24),(75,3699,-1,'2017-03-11 13:36:29',25),(76,1499,-1,'2017-03-11 13:36:29',26),(77,2799,-1,'2017-03-11 13:36:29',27),(78,579,-1,'2017-03-11 13:36:30',28),(79,2199,-1,'2017-03-11 13:36:30',29),(80,1199,-1,'2017-03-11 13:36:30',30),(81,579,-1,'2017-03-11 13:36:30',31),(82,299,-1,'2017-03-11 13:36:30',32),(83,359,-1,'2017-03-11 13:36:30',33),(84,479,-1,'2017-03-11 13:36:31',34),(85,1769,-1,'2017-03-11 13:36:31',35),(86,219,-1,'2017-03-11 13:36:31',36),(87,1099,-1,'2017-03-11 13:36:31',37),(88,1999,-1,'2017-03-11 13:36:31',38),(89,599,-1,'2017-03-11 13:36:31',39),(90,328,-1,'2017-03-11 13:36:31',40),(91,259,-1,'2017-03-11 13:36:32',41),(92,219,-1,'2017-03-11 13:36:32',42),(93,419,-1,'2017-03-11 13:36:32',43),(94,1409,-1,'2017-03-11 13:36:32',44),(95,99,-1,'2017-03-11 13:36:32',45),(96,659,-1,'2017-03-11 13:36:32',46),(97,1199,-1,'2017-03-11 13:36:32',47),(98,669,-1,'2017-03-11 13:36:33',48),(99,328,-1,'2017-03-11 13:36:33',49),(100,259,-1,'2017-03-11 13:36:33',50),(101,219,-1,'2017-03-11 13:36:33',51),(102,419,-1,'2017-03-11 13:36:33',52),(103,1579,-1,'2017-03-11 13:36:33',53),(104,99,-1,'2017-03-11 13:36:33',54),(105,659,-1,'2017-03-11 13:36:34',55),(106,999,-1,'2017-03-31 19:46:05',21),(107,219,-1,'2017-03-31 19:46:05',22),(108,799,-1,'2017-03-31 19:46:06',23),(109,2649,-1,'2017-03-31 19:46:06',24),(110,3699,-1,'2017-03-31 19:46:07',25),(111,1299,-1,'2017-03-31 19:46:07',26),(112,2499,-1,'2017-03-31 19:46:08',27),(113,2099,-1,'2017-03-31 19:46:08',29),(114,1199,-1,'2017-03-31 19:46:08',30),(115,579,-1,'2017-03-31 19:46:09',31),(116,299,-1,'2017-03-31 19:46:09',32),(117,399,-1,'2017-03-31 19:46:09',33),(118,479,-1,'2017-03-31 19:46:09',34),(119,1769,-1,'2017-03-31 19:46:10',35),(120,999,-1,'2017-03-31 19:46:10',37),(121,1949,-1,'2017-03-31 19:46:10',38),(122,599,-1,'2017-03-31 19:46:11',39),(123,328,-1,'2017-03-31 19:46:11',40),(124,219,-1,'2017-03-31 19:46:11',42),(125,1415,-1,'2017-03-31 19:46:12',44),(126,99,-1,'2017-03-31 19:46:12',45),(127,1199,-1,'2017-03-31 19:46:12',47),(128,669,-1,'2017-03-31 19:46:12',48),(129,259,-1,'2017-03-31 19:46:13',50),(130,419,-1,'2017-03-31 19:46:13',52),(131,1579,-1,'2017-03-31 19:46:13',53),(132,659,-1,'2017-03-31 19:46:13',55),(133,999,-1,'2017-04-08 16:21:23',21),(134,219,-1,'2017-04-08 16:21:23',22),(135,799,-1,'2017-04-08 16:21:24',23),(136,2599,-1,'2017-04-08 16:21:24',24),(137,3699,-1,'2017-04-08 16:21:24',25),(138,1299,-1,'2017-04-08 16:21:25',26),(139,2499,-1,'2017-04-08 16:21:26',27),(140,2099,-1,'2017-04-08 16:21:26',29),(141,1199,-1,'2017-04-08 16:21:27',30),(142,579,-1,'2017-04-08 16:21:27',31),(143,299,-1,'2017-04-08 16:21:28',32),(144,399,-1,'2017-04-08 16:21:29',33),(145,479,-1,'2017-04-08 16:21:29',34),(146,1769,-1,'2017-04-08 16:21:30',35),(147,969,-1,'2017-04-08 16:21:31',37),(148,1949,-1,'2017-04-08 16:21:31',38),(149,599,-1,'2017-04-08 16:21:31',39),(150,328,-1,'2017-04-08 16:21:31',40),(151,219,-1,'2017-04-08 16:21:32',42),(152,1408,-1,'2017-04-08 16:21:32',44),(153,99,-1,'2017-04-08 16:21:32',45),(154,1199,-1,'2017-04-08 16:21:33',47),(155,669,-1,'2017-04-08 16:21:33',48),(156,259,-1,'2017-04-08 16:21:33',50),(157,419,-1,'2017-04-08 16:21:34',52),(158,1479,-1,'2017-04-08 16:21:34',53),(159,699,-1,'2017-04-08 16:21:34',55),(160,999,-1,'2017-04-09 17:29:50',21),(161,219,-1,'2017-04-09 17:29:51',22),(162,799,-1,'2017-04-09 17:29:51',23),(163,2599,-1,'2017-04-09 17:29:51',24),(164,3699,-1,'2017-04-09 17:29:51',25),(165,1299,-1,'2017-04-09 17:29:51',26),(166,2499,-1,'2017-04-09 17:29:52',27),(167,2099,-1,'2017-04-09 17:29:52',29),(168,1199,-1,'2017-04-09 17:29:52',30),(169,579,-1,'2017-04-09 17:29:52',31),(170,299,-1,'2017-04-09 17:29:52',32),(171,399,-1,'2017-04-09 17:29:53',33),(172,479,-1,'2017-04-09 17:29:53',34),(173,1769,-1,'2017-04-09 17:29:53',35),(174,969,-1,'2017-04-09 17:29:53',37),(175,1949,-1,'2017-04-09 17:29:53',38),(176,599,-1,'2017-04-09 17:29:54',39),(177,328,-1,'2017-04-09 17:29:54',40),(178,219,-1,'2017-04-09 17:29:54',42),(179,1408,-1,'2017-04-09 17:29:54',44),(180,99,-1,'2017-04-09 17:29:54',45),(181,1199,-1,'2017-04-09 17:29:55',47),(182,669,-1,'2017-04-09 17:29:55',48),(183,259,-1,'2017-04-09 17:29:55',50),(184,419,-1,'2017-04-09 17:29:55',52),(185,1479,-1,'2017-04-09 17:29:56',53),(186,699,-1,'2017-04-09 17:29:56',55);
/*!40000 ALTER TABLE `t_object_history_price` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_suit`
--

DROP TABLE IF EXISTS `t_suit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_suit` (
  `tid` bigint(20) NOT NULL AUTO_INCREMENT,
  `suit_name` varchar(100) NOT NULL,
  `cpu_id` bigint(20) NOT NULL,
  `gpu_id` bigint(20) NOT NULL,
  `ram_id` bigint(20) NOT NULL,
  `power_id` bigint(20) NOT NULL,
  `box_id` bigint(20) NOT NULL,
  `main_board_id` bigint(20) NOT NULL,
  `ssd_id` bigint(20) NOT NULL,
  `hddk_id` bigint(20) NOT NULL,
  `cooler_id` bigint(20) NOT NULL,
  PRIMARY KEY (`tid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_suit`
--

LOCK TABLES `t_suit` WRITE;
/*!40000 ALTER TABLE `t_suit` DISABLE KEYS */;
INSERT INTO `t_suit` VALUES (1,'1060Pro',35,29,34,32,33,30,37,31,22),(2,'1070Pro',24,25,21,23,33,26,27,31,22),(3,'1050Evo',53,47,52,50,42,48,55,40,45),(4,'1060Evo',44,38,52,50,42,39,55,40,45);
/*!40000 ALTER TABLE `t_suit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_suit_history`
--

DROP TABLE IF EXISTS `t_suit_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_suit_history` (
  `tid` bigint(20) NOT NULL,
  `total_price` decimal(10,0) NOT NULL,
  `date` varchar(10) NOT NULL,
  `suit_id` bigint(20) NOT NULL,
  PRIMARY KEY (`tid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_suit_history`
--

LOCK TABLES `t_suit_history` WRITE;
/*!40000 ALTER TABLE `t_suit_history` DISABLE KEYS */;
/*!40000 ALTER TABLE `t_suit_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_type`
--

DROP TABLE IF EXISTS `t_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_type` (
  `tid` bigint(20) NOT NULL AUTO_INCREMENT,
  `type_desc` varchar(25) NOT NULL DEFAULT ' ',
  PRIMARY KEY (`tid`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_type`
--

LOCK TABLES `t_type` WRITE;
/*!40000 ALTER TABLE `t_type` DISABLE KEYS */;
INSERT INTO `t_type` VALUES (1,'CPU'),(2,'显卡'),(3,'内存'),(4,'电源'),(5,'机箱'),(6,'主板'),(7,'固态'),(8,'机械'),(9,'散热器');
/*!40000 ALTER TABLE `t_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `v_obj_history`
--

DROP TABLE IF EXISTS `v_obj_history`;
/*!50001 DROP VIEW IF EXISTS `v_obj_history`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `v_obj_history` AS SELECT 
 1 AS `时间`,
 1 AS `商品ID`,
 1 AS `商品名`,
 1 AS `类型`,
 1 AS `价格`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `suit_his_price`
--

/*!50001 DROP VIEW IF EXISTS `suit_his_price`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `suit_his_price` AS select concat(`suit`.`tid`,`obj_his`.`tid`) AS `id`,`suit`.`suit_name` AS `套装`,`obj`.`type_name` AS `类型`,`obj`.`obj_name` AS `品名`,`obj_his`.`price` AS `价格`,`obj_his`.`gmt_create` AS `时间` from ((`t_suit` `suit` join `t_object_history_price` `obj_his` on(((`suit`.`cpu_id` = `obj_his`.`obj_id`) or (`suit`.`gpu_id` = `obj_his`.`obj_id`) or (`suit`.`ssd_id` = `obj_his`.`obj_id`) or (`suit`.`hddk_id` = `obj_his`.`obj_id`) or (`suit`.`ram_id` = `obj_his`.`obj_id`) or (`suit`.`box_id` = `obj_his`.`obj_id`) or (`suit`.`cooler_id` = `obj_his`.`obj_id`) or (`suit`.`main_board_id` = `obj_his`.`obj_id`) or (`suit`.`power_id` = `obj_his`.`obj_id`)))) join `t_object` `obj` on((`obj_his`.`obj_id` = `obj`.`tid`))) order by `suit`.`suit_name` desc,`obj`.`type_name`,`obj_his`.`gmt_create` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_obj_history`
--

/*!50001 DROP VIEW IF EXISTS `v_obj_history`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_obj_history` AS select `price`.`gmt_create` AS `时间`,`obj`.`jkuid` AS `商品ID`,`obj`.`obj_name` AS `商品名`,`obj`.`type_name` AS `类型`,`price`.`price` AS `价格` from (`t_object` `obj` left join `t_object_history_price` `price` on((`price`.`obj_id` = `obj`.`tid`))) order by `obj`.`jkuid`,`price`.`gmt_create` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-04-09 17:31:06
