/*
SQLyog Ultimate v13.1.1 (64 bit)
MySQL - 10.4.22-MariaDB : Database - squad_test
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`squad_test` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `squad_test`;

/*Table structure for table `joke` */

DROP TABLE IF EXISTS `joke`;

CREATE TABLE `joke` (
  `number` int(11) NOT NULL AUTO_INCREMENT,
  `joke` varchar(100) NOT NULL,
  `active` int(1) NOT NULL DEFAULT 1,
  PRIMARY KEY (`number`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `joke` */

insert  into `joke`(`number`,`joke`) values (2,'Nuevo chiste');
insert  into `joke`(`number`,`joke`) values (3,'eeee mundo errr');
insert  into `joke`(`number`,`joke`) values (4,'eeee mundo errr');
insert  into `joke`(`number`,`joke`) values (6,'weeeeeeeee');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
