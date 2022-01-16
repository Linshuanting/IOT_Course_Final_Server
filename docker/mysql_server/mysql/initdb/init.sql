create database userTable;
create table userTable.USER_DATA(
    myUSER varchar(40),
    myTABLE varchar(40),
    PRIMARY KEY(myUSER)
);

create database fileDataBase;
create table fileDataBase.people (
    ID int NOT NULL AUTO_INCREMENT,
    goods varchar(20), 
    price int(40),
    category varchar(20),
    spendTime varchar (30),
    remark varchar(50),
    PRIMARY KEY(ID));
insert into fileDataBase.people(goods, price, category, spendTime, remark) 
    values ('apple', 50, '零食', '12/12', '有點貴');
insert into fileDataBase.people(goods, price, category, spendTime, remark)
    values ('banana', 30, '晚餐', '12/12', '節食中');
insert into fileDataBase.people(goods, price, category, spendTime, remark) 
    values ('coconat', 16, '早餐', '12/13', 'I love coconat milk');
