# Flask Agency Website
[inspiration_link]:https://www.templatemonster.com/joomla-templates/sombra-black-amp-color-multipurpose-joomla-template-247716.html
A simple implementation of an agency website to carry out campaign on the company reputation, services offered and the activities that carry along in the company profile. [Inspiration]([inspiration_link])

---

## Table of contents
1. [Introduction](#introduction)
2. [Project installation and development](#installation)
3. [Another paragraph](#paragraph2)

## This is the introduction <a name="introduction"></a>
Some introduction text, formatted in heading 2 style

## Installation <a name="installation"></a>
># Prerequesites
> Installed `nodejs` and `python` globally in your system
> Next we need `nodejs` package known as `nodemon` installed if possible globally in the system

First of all clone the repository using
```sh
git clone <repo_link> agency_website
```
Once the project is cloned, navigate to the agency website folder by `cd agency_website`. Since the website will run on both `Flask` and `nodejs` to transpile `tailwindcss` and `flask` running the backend server. `concurrently` nodejs package helps us to easily run concurrent scripts to facilitate development and hot reload of `tailwind` transpilation.

There are a couple `npm` scripts to be run but initially well start by

-  Creating a virtualenv using the following
```sh
pipenv shell
``` 
- Install all the modules from `requirements.txt` using 
```sh
pipenv install -r requirements.txt
```
- Install `node_modules` using `npm install` or `yarn` or `pnpm i`


Once the modules are in place, we'll use the `npm scripts` to run the application

`dev` - Running all the development scripts via concurrently

`dev:server`  - Running the flask app independently

`dev:tailwind` - Transpiling tailwindcss utitlity classes

### Sub paragraph <a name="subparagraph1"></a>
This is a sub paragraph, formatted in heading 3 style

## Another paragraph <a name="paragraph2"></a>
The second paragraph text

----

