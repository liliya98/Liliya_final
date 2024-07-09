﻿
# Представляю вашему вниманию Liliya_project
# Это мой дипломный проект на курсе Инженер по тестированию +
# Яндекс Практикум


- Для запуска тестов должны быть установлены пакеты `pytest` и `requests`.
- Запуск всех тестов выполняется командой `pytest`.


# 1. Работа с базой данных
Запросы расположены в файле Base.sql 

Задание 1
Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных.
Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true). 

запрос:

          SELECT c.login, COUNT(o.id) AS "deliveryCount" 
          FROM "Couriers" AS c 
          LEFT JOIN "Orders" AS o ON c.id = o."courierId" 
          WHERE o."inDelivery" = true 
          GROUP BY c.login;

Скриншот результата запроса database2.png.png 

Задание 2

Ты тестируешь статусы заказов. Нужно убедиться, что в базе данных они записываются корректно.
Для этого: выведи все трекеры заказов и их статусы. 
Статусы определяются по следующему правилу:
Если поле finished == true, то вывести статус 2.
Если поле canсelled == true, то вывести статус -1.
Если поле inDelivery == true, то вывести статус 1.
Для остальных случаев вывести 0.

запрос:

           SELECT track, 
              CASE 
	        WHEN finished = true THEN 2 
	        WHEN cancelled = true THEN -1 
	        WHEN "inDelivery" = true THEN 1 
	  ELSE 0 END AS status 
          FROM "Orders";

Скриншот результата запроса database.png.png
# 2. Автоматизация теста.

Для запуска теста необходимо в файл configuration скопировить URLстенда вида 
https://ce07c5c3-b44d-4640-961d-a073435e7da3.serverhub.praktikum-services.ru

В файле test нажать кнопку Run 

Скриншот автоматизации  Autotest.png 

### Стек для выполнения проекта

* PyCharm
* GitHub

* requests
* pytest

## Автор

Лилия Переплетчикова, 18 когорта