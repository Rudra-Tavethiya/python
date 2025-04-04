create database 1_fab;
use 1_fab;

create table student(
id int primary key auto_increment,
name varchar(20),
email varchar(50)
);

alter table student add column (phone int);
alter table student modify phone varchar(10);
alter table student drop column phone;
alter table student rename to data;

truncate data;
drop table data;

drop table student;




insert into data values(0,'rudra','r@gmail.com');
insert into data(name) values('rudra');
insert into data(email) values('rt@gmail.com');

update data set email='rt@gmail.com' where id=2;

delete from data where id=3;




CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    email VARCHAR(50),
    dept VARCHAR(30),
    sal DECIMAL(10,2)
);
INSERT INTO employees (id, name, age, email, dept, sal) VALUES
(1, 'Amit Sharma', 28, 'amit.sharma@example.com', 'IT', 60000.00),
(2, 'Priya Mehta', 25, 'priya.mehta@example.com', 'HR', 50000.00),
(3, 'Rahul Verma', 30, 'rahul.verma@example.com', 'Finance', 70000.00),
(4, 'Suman Roy', 26, 'suman.roy@example.com', 'Marketing', 55000.00),
(5, 'Karan Singh', 29, 'karan.singh@example.com', 'IT', 62000.00),
(6, 'Neha Gupta', 24, 'neha.gupta@example.com', 'HR', 48000.00),
(7, 'Vikram Batra', 32, 'vikram.batra@example.com', 'Sales', 75000.00),
(8, 'Sneha Patil', 27, 'sneha.patil@example.com', 'Finance', 65000.00),
(9, 'Anil Yadav', 31, 'anil.yadav@example.com', 'Marketing', 58000.00),
(10, 'Ritika Jain', 26, 'ritika.jain@example.com', 'IT', 61000.00),
(11, 'Deepak Chawla', 29, 'deepak.chawla@example.com', 'HR', 52000.00),
(12, 'Pooja Reddy', 28, 'pooja.reddy@example.com', 'Finance', 67000.00),
(13, 'Rohit Mishra', 30, 'rohit.mishra@example.com', 'Sales', 72000.00),
(14, 'Tina DSouza', 27, 'tina.dsouza@example.com', 'Marketing', 56000.00),
(15, 'Siddharth Malhotra', 33, 'siddharth.m@example.com', 'IT', 68000.00),
(16, 'Komal Joshi', 25, 'komal.joshi@example.com', 'HR', 49000.00),
(17, 'Arjun Nair', 29, 'arjun.nair@example.com', 'Finance', 71000.00),
(18, 'Meera Pillai', 26, 'meera.pillai@example.com', 'Marketing', 57000.00),
(19, 'Yashwant Rao', 30, 'yashwant.rao@example.com', 'Sales', 74000.00),
(20, 'Divya Kapoor', 27, 'divya.kapoor@example.com', 'IT', 63000.00);

alter table employees rename emp;
select * from emp;
select name,email from emp;
select distinct(dept) from emp;

select * from emp where dept='hr';
select * from emp where dept='hr' or dept='sales';
select * from emp where dept='hr' and sal>49000;

select * from emp where dept in ('hr','sales','it');
select * from emp where dept not in ('hr');

select * from emp where name like 's%';
select * from emp where name like '%i';
select * from emp where name like '_a%';
select * from emp where name like '__r%';

select * from emp order by age;
select * from emp order by age desc;

select * from emp limit 0,3;
select * from emp limit 5,3;

select sum(sal) as total_salary from emp;
select avg(sal) from emp;
select min(sal) from emp;
select max(sal) from emp;

select count(distinct(dept)) from emp;

#max salary
select * from emp where sal=(select max(sal) from emp);

#seconf highest sallary
select * from emp where sal=(select max(sal) from emp where sal < (select max(sal) from emp));

select * from emp order by sal desc limit 1,1;

select max(sal),dept from emp group by dept;




start transaction;
delete from emp where id=1;
savepoint a;
update emp set age=30 where id=2;
select * from emp;
rollback;



create table author(aid int primary key auto_increment, aname varchar(20));

create table publisher(pid int primary key auto_increment, pname varchar(20));

create table book(id int primary key auto_increment, aid int, pid int, foreign key(aid) references author(aid),
																		foreign key(pid) references publisher(pid));



select * from book join author on book.aid=author.aid;

select book.bname,author.aname from book join author on book.aid=author.aid;

select b.bname,a.aname from book b join author a on b.aid=a.aid;

select b.bname,a.aname from book b left join author a on b.aid=a.aid;

select b.bname,a.aname from book b right join author a on b.aid=a.aid;

select b.bname,a.aname from book b right join author a on b.aid=a.aid
union
select b.bname,a.aname from book b left join author a on b.aid=a.aid;




create view allbook as select * from book;



delimiter //
create procedure allemp()
begin
	select * from emp;
end //
call allemp();

delimiter //
create procedure agebyid(in eid int)
begin
	select age from emp where id=eid;
end //
call agebyid(5);

delimiter //
create procedure total_sal(out t_sal int)
begin
	select sum(sal) into t_sal from emp;
end //
call total_sal(@t);
select @t as total_sallary;

delimiter //
create procedure total_dept1(out t_dep int)
begin
	select count(distinct(dept)) into t_dep from emp;
end //
call total_dept1(@t);
select @t as total_department;

delimiter //
create procedure agebyid8(inout a int)
begin
	select age into a from emp where id=a;
end //
set @b = 8;
call agebyid8(@b);
select @b;


create table emplog(id int primary key auto_increment, eid int, name varchar(20), email varchar(50), sal double); 

delimiter //
create trigger amplog before delete on emp for each row
begin
	insert into emplog (eid, name, email, sal) values (old.id,old.name,old.email,old.sal);
end;

delete from emp where id = 5;


