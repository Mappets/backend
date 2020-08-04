<!-- PROJECT LOGO -->
<p align="center">
  <a href="https://github.com/Mappets">
    <img src="https://raw.githubusercontent.com/Mappets/assets/master/brand/brand-colored.png" width="350px" alt="Mappets brand">
  </a>

  <h3 align="center">We care a lot about animals.</h3>
</p>

---

## Contributing Guide

## Before you start

Please, make sure you have read the project description. If don't, read rigth [clicking here](https://github.com/Mappets/backend/blob/master/README.md).

## Installing

As our stack is not a simple one we opted for standardizing our instructions do [Docker Compose](https://docs.docker.com/compose/install/), which will help you spin up every service in a few commands.

### Running

Example to run only the back-end:

```console
make up
```

if you had execute the application before some stuffs had changed. Then you should to execute to clear the database migrations:

```console
docker-compose -p mappets run --rm django python manage.py reset_db
```

Then browse from [`localhost:8000`](http://localhost:8000).

## The basics of contributing

A lot of discussions about ideas take place in the [Issues](https://github.com/Mappets/backend/issues) section.

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
