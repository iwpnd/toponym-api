# Toponym-API

API for [Toponym](https://github.com/iwpnd/toponym) built with the amazing [FastAPI](https://fastapi.tiangolo.com). 

# Description 

In slavic languages a word can change, depending on how and where it is used within a sentence. The city Moscow (`Москва`) changes to `Москве` when used prepositional. 


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installing

```
git clone https://github.com/iwpnd/toponym-api.git
```

````
docker build -t toponym-api .
docker run -d --name toponym-api-container -p 80:80 toponym-api
```

## Running the tests

soon

```
python -m pytest .
```

## Usage

See `/docs` or `scripts/example.ipynb`

## Authors

* **Benjamin Ramser** - *Initial work* - [iwpnd](https://github.com/iwpnd)

See also the list of [contributors](https://github.com/iwpnd/toponym/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

