![Github](https://img.shields.io/github/license/dapingtai/Affy-ETL?style=for-the-badge)
![pypi](https://img.shields.io/pypi/v/Affy-ETL?style=for-the-badge)
# Affy-ETL
### Easy to extract, transform and loading AffyData to MySQL

## Installation
- [Finish install requirement package](https://github.com/dapingtai/Affy-ETL/blob/master/requirements.txt)
- Python
```python
pip install Affy-ETL
```
- R
```R
install.package("BiocManager")
BiocManager::install("affy")
BiocManager::install("affyio")
```
  * The annotation data (cdf)
    * http://bioconductor.org/packages/release/BiocViews.html#___cdf
      * Affy Human Genome U133 Plus 2.0 Array
      ```
      BiocManager::install("hgu133plus2cdf")
      ```
      * Affy Mouse Genome 430 2.0 Array
      ```
      BiocManager::install("mouse430a2cdf")
      ```
## Usage Processing

### 1.Extract
- Choose the file path of microarray data(.CEL) 
- Choose the annotation of microarray platform(cdf)
```python
from Affy_ETL import AETL
data, data_len = AETL.extract(dir="Your CEL dir",cdf="Your cdf name") 
```
### 2.Transform
```python
transform_data = AETL.transform(data, data_len)
```
### 3.Loading
```python
AETL.loading(user="****", passwd="****", address="Your database Ip", dbname="****", tablename="****", data = transform_data)
```
