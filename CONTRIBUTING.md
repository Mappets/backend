# Mappets

Contributing Guide

## Before you start

Please, make sure you have read the project description. If don't, read rigth [clicking here]().

## Installing

As our stack is not a simple one we opted for standardizing our instructions do [Docker Compose](https://docs.docker.com/compose/install/), which will help you spin up every service in a few commands.

Everything is expected to work with:

```console
$ docker-compose up
```

**Note:** `docker-compose up` is just a health check to assure all dependencies are succesfully installed and the project is running well. To run properly Mappets there are a few more steps (migrations, for example), which are the ones below.

### Running

Example to run only the back-end:

```console
$ docker-compose run —rm web pip install -r requirements.txt
$ docker-compose app python manage.py
$ docker-compose app python manage.py createsuperuser
```

The spin up the web server:

```console
$ docker-compose up -d
```

Then browse from [`localhost`](http://localhost).

## The basics of contributing

A lot of discussions about ideas take place in the [Issues](https://github.com/Mappets/website/issues) section.

### The Git basics

**1. _Fork_ this repository**

There's a big button for that in GitHub interface, usually on the top right corner.

**2. Clone your fork of the repository**

```console
$ git clone http://github.com/<YOUR-GITHUB-USERNAME>/website.git
```

**3. Create a feature branch**

```console
$ git checkout -b <YOUR-GITHUB-USERNAME>-new-stuff
```

Please, note that we prefix branch names with GitHub usernames, this helps us in keeping track of changes and who is working on them.

**4. Do what you do best**

Now it's your time to shine and write meaningful code to raise the bar of the project!

**5. Commit your changes**

```console
$ git commit -am 'My pretty cool contribution'
```

**6. Push to the branch to your fork**

```consle
$ git push origin <YOUR-GITHUB-USERNAME>-new-stuff
```

**7. Create a new _Pull Request_**

From your fork at GitHub usually there is a button to open pull requests.
