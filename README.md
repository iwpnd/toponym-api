# Toponym-API

API for [Toponym](https://github.com/iwpnd/toponym) built with the amazing [FastAPI](https://fastapi.tiangolo.com).

# Description

In slavic languages a word can change, depending on how and where it is used within a sentence. The city Moscow (`Москва`) changes to `Москве` when used prepositional. See [toponym](https://github.com/iwpnd/toponym).


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installing

```
git clone https://github.com/iwpnd/toponym-api.git
```

```
docker build -t toponym_api .
docker run -d --name toponym-api-container -p 80:80 toponym_api
```

## Running the tests

```
git clone https://github.com/iwpnd/toponym-api.git
cd toponym-api
pip install poetry
poetry install
pytest -v
```

## Deployment

see blogpost

## Authors

* **Benjamin Ramser** - *Initial work* - [iwpnd](https://github.com/iwpnd)

See also the list of [contributors](https://github.com/iwpnd/toponym-api/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
