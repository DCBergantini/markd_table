# Markdown

Cria template de documentação de tabelas em markdown a partir de um arquivo tabular csv ou excel.

## Setup

Install the dependencies with…

```
pip3 install -r requirements.txt
```

## Running

Running the following command…

```
$ python3 src/main.py -s examples/demo.csv
```

…outputs the following markdown…

```
# Demo

DESCRIPTION

## Model

| Column     | Type | Example Value | Description | Format |
| :--------- | :--- | :------------ | :---------- | :----- |
| Name       | TYPE | Jon Doe       | DESCRIPTION | FORMAT |
| Phone      | TYPE | 999001216     | DESCRIPTION | FORMAT |
| Birth Date | TYPE | 2022-01-14    | DESCRIPTION | FORMAT |
| Net Worth  | TYPE | 100000000     | DESCRIPTION | FORMAT |
```
Check the help command…

```
python3 src/main.py --help
```
