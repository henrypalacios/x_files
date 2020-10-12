# X Files

A scrapy project for scraping declassified documents.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

- python3.6+
- pip
- python3-venv

### Installing

- **Unix Systems using make**

1. create virtual enviroment and install the dependencies.  
    ```bash
    make
    ```

2. activate enviroment
    ```bash
    source .venv_py/bin/activate
    ```

- **Manual mode**
1. Create virtual enviroment  
`python3 -m venv .venv_py`  
2. Activate  
`source .venv_py/bin/activate`
3. Opgrade pip (optional)   
`python3 -m pip install --upgrade pip`
4. Install dependencies  
`pip install -r requirements.txt requirements-dev.txt`


## Built With

* [scrapy](https://scrapy.org/) - The framework for extracting data

## License

This project is licensed under the MIT License.
