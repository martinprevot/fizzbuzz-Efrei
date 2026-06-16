# FizzBuzz — Efrei

![Tests](https://github.com/martinprevot/fizzbuzz-Efrei/actions/workflows/tests.yml/badge.svg)

Implémentation classique de FizzBuzz en Python, avec tests unitaires (`unittest`) et intégration continue via GitHub Actions.

## Le principe

Pour les nombres de 1 à *n* :
- multiple de 3 → `Fizz`
- multiple de 5 → `Buzz`
- multiple de 3 **et** 5 → `FizzBuzz`
- sinon → le nombre lui-même

## Structure

```
fizzbuzz-Efrei/
├── main.py                      # la fonction fizzbuzz
├── Dockerfile
├── test/
│   ├── __init__.py
│   └── testunitaire.py          # tests unittest
└── .github/workflows/tests.yml  # CI GitHub Actions
```

## Lancer le programme

```bash
python main.py
```

## Lancer les tests

Depuis la racine du projet :

```bash
python -m unittest discover -s test -p "testunitaire.py"
```

Option verbeuse pour voir le détail de chaque test :

```bash
python -m unittest discover -s test -p "testunitaire.py" -v
```

## Intégration continue

À chaque `push` ou *pull request* sur `main`, GitHub Actions exécute automatiquement les tests. Le statut est visible via le badge en haut de ce README et dans l'onglet **Actions** du dépôt.

## Docker

```bash
docker build -t fizzbuzz .
docker run --rm fizzbuzz
```
