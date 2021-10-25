# Shopping Organizer

## Application Description:
This is a web application designed to make the shopping and grocery planning experience a breeze. This web app can be used to manage and store recipes, lists (shopping, to-do, etc.), and in the future, your kitchen/ pantry inventory.

The intended future goal is to also receive recommendations of recipes that you already have ingredients for in your own personal pantry, or that require purchasing the fewest additional ingredients. Also intended, is for the app to alert ingredients are low or need to be purchased in your personal pantry.


## Software Used:
- Python 3.9
- Django 3.2
- PostgreSQL (using psycopg2 2.9.1)
- Docker/ Docker-compose
- Bootstrap 5.1


## Features:

### Currently Implemented
- [x] Connect PostgreSQL to Django app :heavy_check_mark:
- [x] Docker/ docker-compose for django and postgres :heavy_check_mark:
- [x] Bootstrap for responsive design :heavy_check_mark:
- [x] Create, delete, and edit multiple shopping lists' names and budgets :heavy_check_mark:
- [x] Create, delete, and edit shopping list items' name and price :heavy_check_mark:
- [x] Basic Django logging and info logging :heavy_check_mark:
- [x] User registration, authentication, and login :heavy_check_mark:
- [x] Friend requests with ability to cancel, decline, or accept :heavy_check_mark:
- [x] Friend list with ability to remove friends :heavy_check_mark:
- [x] Share lists with friends :heavy_check_mark:
- [x] View and differentiate current user's lists and shared lists from others :heavy_check_mark:

### Near Future Implementations:
- [ ] Authentication with email verification :clock1:
- [ ] Show verbose item info, check off bought items, and filter items by `checked_off` :clock1:
- [ ] Edit user profile (user portrait, password, name, and email) :clock1:
- [ ] Unit tests :clock1:
- [ ] Cache :clock1:
- [ ] Implement Django Rest framework :clock1:
- [ ] Implement react and make front-end beautiful :clock1:
- [ ] Error Handling :clock1:
- [ ] Unit tests :clock1:
- [ ] Documentation :clock1:
- [ ] Deploy :clock1:

### Hopeful Future Implementations:
- [ ] Kitchen/pantry inventory system :thought_balloon:
- [ ] Recipes (webscraped for convenience and user created) :thought_balloon:
- [ ] Machine learning to suggest (and add to shopping list) kitchen inventory to be replenished :thought_balloon:
- [ ] Machine learning to suggest recipes based off of either past food choices or desired cuisine type, considering factors such as available kitchen inventory, time available, and price of needed items :thought_balloon:

## Installing and Running

1. Install [Docker-compose](https://docs.docker.com/compose/install/).

2. Clone the [shopping-organizer](https://github.com/stephenrobic/shopping-organizer) repository.
    ```shell
    git clone https://github.com/stephenrobic/shopping-organizer.git
    ```

3. Create an `.env` file in the parent directory (shopping-organizer), containing the following:
    ```
    DJANGO_SUPERUSER_USERNAME=user
    DJANGO_SUPERUSER_PASSWORD=password
    DJANGO_SUPERUSER_EMAIL=youremail@email.com
    DATABASE_ENGINE=django.db.backends.postgresql
    DATABASE_USER=postgres
    DATABASE_NAME=postgres
    DATABASE_HOST=db
    DATABASE_PORT=5432
    ```
    **NOTE**: For `DJANGO_SUPERUSER_EMAIL`, change `youremail@email.com` to your preferred email address. The `DJANGO_SUPERUSER_USERNAME` and `DJANGO_SUPERUSER_PASSWORD` will be used to log in to the Django admin site ([http://0.0.0.0:8000/admin](http://0.0.0.0:8000/admin)).

4. Within this same parent directory, use the following command to build the images and start the containers:
    ```shell
    docker-compose up -d --build
    ```
    This will create docker "containers", containing the shopping-list and postgres database images.

    **NOTE**: The `-d` option runs containers detached in the background; you may find it useful to exclude this, as you will be able to note information about the building. The `--build` option builds the images (postgres alpine server and shopping list app), before starting the containers.

6. In your browser, go to [http://0.0.0.0:8000](http://0.0.0.0:8000) to launch the application. Voilà!
