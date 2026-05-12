SIT_2_yatabe
1. Добавил изображения к постам
2. Расширил стандартного пользователя через отдельную модель профиля (UserProfile) с полями:
  - `avatar` — фото профиля
  - `bio` — информация о себе
  - `city` — город
  - `birth_date` — дата рождения
  - `hobbies` — увлечения
  - `education` — образование
  - `website` — личный сайт
  <img width="468" height="114" alt="image" src="https://github.com/user-attachments/assets/b1ac0a89-d2dd-4f5f-8d42-4ab11308a333" />
  Форма создания поста с загрузкой изображения
  <img width="468" height="210" alt="image" src="https://github.com/user-attachments/assets/54e8b6f0-2ba6-4163-8a3a-27342547bde4" />
  API возвращает полный URL загруженного изображения
  <img width="468" height="192" alt="image" src="https://github.com/user-attachments/assets/e949ae6d-8dd8-4101-b5bc-e27780e02a99" />
  Заполнение расширенных полей профиля (аватар, город, био)
  <img width="468" height="175" alt="image" src="https://github.com/user-attachments/assets/8447e04d-dbd2-4726-a639-98a34fa93dde" />
  Успешное обновление профиля пользователя
  <img width="468" height="200" alt="image" src="https://github.com/user-attachments/assets/80e135fe-d3fc-490e-afe3-d475fc41f571" />
  В ответе поста отображается расширенная информация об авторе (author_profile)



