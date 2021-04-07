-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 02, 2021 at 08:53 PM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `educationia`
--

-- --------------------------------------------------------

--
-- Table structure for table `class_10`
--

CREATE TABLE `class_10` (
  `sno` int(11) NOT NULL,
  `clas` varchar(5) NOT NULL,
  `year` varchar(4) NOT NULL,
  `subject` varchar(30) NOT NULL,
  `url` varchar(300) NOT NULL,
  `date` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `class_10`
--

INSERT INTO `class_10` (`sno`, `clas`, `year`, `subject`, `url`, `date`) VALUES
(16, '10', '2017', 'English', 'https://d2cyt36b7wnvt9.cloudfront.net/exams/wp-content/uploads/2018/02/13172800/CBSE-Class-10-English-Question-Paper-20171.pdf', '2021-03-07'),
(17, '10', '2018', 'English', 'https://d2cyt36b7wnvt9.cloudfront.net/exams/wp-content/uploads/2018/02/12163801/CBSE-Class-10-English-Question-Paper-2018-embibe.pdf', '2021-03-07'),
(18, '10', '2019', 'English', 'https://d2cyt36b7wnvt9.cloudfront.net/exams/wp-content/uploads/2019/02/28115217/CBSE-Class-10-English-Lang-and-Lit-Paper-2019.pdf', '2021-03-07'),
(19, '10', '2017', 'Maths', 'https://d2cyt36b7wnvt9.cloudfront.net/exams/wp-content/uploads/2018/02/13174433/CBSE-Class-10-Maths-Question-Paper-20171.pdf', '2021-03-07'),
(20, '10', '2018', 'Maths', 'https://d2cyt36b7wnvt9.cloudfront.net/exams/wp-content/uploads/2018/11/20105932/CBSE-Class-10-Maths-Question-Paper-2018.pdf', '2021-03-07'),
(21, '10', '2019', 'Maths', 'https://d2cyt36b7wnvt9.cloudfront.net/exams/wp-content/uploads/2019/02/28133207/CBSE-Class-10-Maths-Question-Paper-2019.pdf', '2021-03-07');

-- --------------------------------------------------------

--
-- Table structure for table `class_12`
--

CREATE TABLE `class_12` (
  `sno` int(11) NOT NULL,
  `clas` varchar(5) NOT NULL,
  `year` varchar(4) NOT NULL,
  `subject` varchar(30) NOT NULL,
  `url` varchar(300) NOT NULL,
  `date` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `class_12`
--

INSERT INTO `class_12` (`sno`, `clas`, `year`, `subject`, `url`, `date`) VALUES
(4, '12', '2017', 'English', 'https://www.cbse.gov.in/cbsenew/question-paper/2017/XII/eng_core.rar', '2021-03-07'),
(5, '12', '2018', 'English', 'https://www.cbse.gov.in/cbsenew/question-paper/2018/XII/english.zip', '2021-03-07'),
(6, '12', '2019', 'English', 'https://www.cbse.gov.in/cbsenew/question-paper/2019/XII/ENGLISH%20CORE.zip', '2021-03-07'),
(7, '12', '2020', 'English', 'https://www.cbse.gov.in/cbsenew/question-paper/2020/XII/English%20Core.zip', '2021-03-07');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `class_10`
--
ALTER TABLE `class_10`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `class_12`
--
ALTER TABLE `class_12`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `class_10`
--
ALTER TABLE `class_10`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `class_12`
--
ALTER TABLE `class_12`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
