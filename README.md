# Education_MSA_develop
**[4차 산업 혁명 선도인력 양성과정]** <br>
**융복합 프로젝트형 클라우드(MSA) 서비스 개발** <br>
2020/07/13 ~ 2020/12/24<br>

* [Class for First project] :: 2020/07/14 ~ 2020/08/10<br>
* [First project] :: 2020/08/11 ~ 2020/08/31<br>
<a href = 'https://blog.naver.com/vega2k'>Teacher's blog</a>

### Pre-Project
<pre>
<h4><a href = "./django_project">Django web framework</a></h4>
</pre>

## TODO
<pre>
<h4>Web scraping</h4>
<del>1. Naver News title search</del>
<del>2. Naver API (papago translation API)</del>
<del>3. Naver webtoon download & upload</del>
<del>4. Weather forecast data search (with beautifulsoup API)</del>
<del>5. Korea Administrative area data analysing (with pandas API, csv data handling)</del>
<del>6. Melon 100 chart</del>
<del>7. Korea congressman search</del>
<del>(6,7)(Using APIs :: Requests, beautifulsoup, pandas, matplotlib, seaborn, pymysql(MariaDB), sqlalchemy)</del>
<del>8. 팟빵(download mp4)</del>
<del>9. Cine21 > movie, actor search (with MongoDB)</del>
</pre>

## Today I Learn [Study for first project (Python)]
<pre>
- Day_1~ Day_3  :   Basic python grammars<br>

<a href = "./Practice/Day_004">- Day_4</a>         :   class & object
                    module & import & package
                    exception handling
                    logging(*)  & file processing

<a href = "./Practice/Day_005">- Day_5</a>         :   pickle
                    Anaconda python & APIs
                    Jupyter
                    Web scraping basic Exercise (with Jupyter)
                    (<a href = "./Practice/Day_005/NHN_service_search.ipynb">News titles scraping</a>, <a href = "./Practice/Day_005/NHN_service_search.ipynb">Use Naver papago API</a>)

<a href = "./Practice/Day_006">- Day_6</a>         :   HTTP method
                    Web scarping (with BeautifulSoup API)(
                        <a href = "./Practice/Day_006/NHN_webtoon_scraper.ipynb">Naver webtoon</a>
                            -> Use CSS selector in BEautifulSoup
                            -> Download im
                            ages and titles etc
                    )

<a href = "./Practice/Day_007">- Day_7</a>         :   More about BeautifulSoup API function
                    Basic of Regular Expression
                    <a href = "./Practice/Day_007/weather_web_scraping.ipynb">Get(download) weather forecast data from web</a>
                    <a href = "./Practice/Day_007/my_weather.json">And make that to JSON file</a>
                    <a href = "./Practice/Day_007/table_practice.html">Practice HTML basic a little bit</a>
                    <a href = "./Practice/Day_007/pandas_ex.ipynb">CSV file analysing with Pandas API</a>

<a href = "./Practice/Day_008">- Day_8</a>         :   <a href = "./Practice/Day_008/pandas_cont.ipynb">Continue Pandas API</a> and <a href = "./Practice/Day_008/pandas_ex.ipynb">Practice</a>
                    <a href = "./Practice/Day_008/matplotlib_ex.ipynb">Matplotlib API</a>
                    Database install >> <a href = "./Practice/Day_008/pymysql_ex.ipynb">Pymysql API</a>

<a href = "./Practice/Day_009">- Day_9</a>         :   <a href = "./Practice/Day_009/melon_scraping.ipynb">Melon top 100 chart scraping(BeautifulSoup API)</a>
                    <a href = "./Practice/Day_009/congressman_scarping.ipynb">Collecting korea congressman data from web(BeautifulSoup API)</a>
                    <a href = "./Practice/Day_009/congressman_scarping.ipynb">And analysing that with Pandas API</a>

<a href = "./Practice/Day_010">- Day_10</a>        :   <a href="./Practice/Day_010/query_ex.md">SQL query Basics</a>
                    <a href = "./Practice/Day_010/melon_songs_to_db.ipynb">JSON to Pandas data frame</a>
                    <a href ="./Practice/Day_010/congressman_cont.ipynb">DB <-> Pandas data frame</a>

<a href = "./Practice/Day_011">- Day_11</a>        :   <a href = "./Practice/Day_011/sql_ex.md">More SQL Basics </a>
                    <a href = "./Practice/Day_011/pymysql_ex.ipynb">Use pymysql API : PL <-> DB</a>
                    <a href = "./Practice/Day_011/web_scraping_mp3_podbbang">Podbbang web scraping (single page)</a>
                    <a href = "./Practice/Day_011/advanced_web_scraping_mp3_podbbang">Podbbang web scraping (multiple pages)</a>
  
<a href = "./Practice/Day_012">- Day_12</a>        :   <a href = "./Practice/Day_012/selenium_ex.ipynb">Selenium Basic</a>
                    <a href = './docs/mongodb_pymongo/1.mongodb_basic_open.ipynb'>MongoDB</a>
                    <a href = '/Practice/Day_012/mongoDB_sql_ex.md'>MongoDB query exercise</a>
                    
<a href = "./Practice/Day_013">- Day_13</a>        :   <a href = "./Practice/Day_013/mongodb_sql_aggregate_ex.md">Aggregation in mongoDB(NoSQL)</a>
                    <a href = "./Practice/Day_013/pymongo_basic.ipynb">Pymongo Basic</a> and
                    <a href = "./Practice/Day_013/json_to_mongodb_and_use.ipynb">JSON to mongoDB and Handling with pymongo</a>
                    
<a href = "./Practice/Day_014">- Day_14</a>        :   <a href = "./Practice/Day_014/pymongo_ex.ipynb">More pymongo(USA post code data)</a>
                    <a href = "./Practice/Day_014/cine21_web_scrap.ipynb">Cine21 web scraping</a> and
                    <a href = "./Practice/Day_014/cine21_web_scrap_advance.ipynb">Advance version(several pages)</a> and
                    <a href = "./Practice/Day_014/actor.json">store that to json file</a>
                    
<a href = "./Practice/Day_015">- Day_15</a>        :   <a href = "./Practice/Day_015/cine21_data_to_db.ipynb">Store Cine21 data to DB and handling</a>
                    <a href = "./django_project">Start of Django</a> and 
                    <a href = "./django_project/django_ex.md">Study about that</a>

<a href = "./django_project">- Day_16</a>        :   Django Simple Project
                    Create Django project and basics
                    MVT pattern
                    CSS, Bootstrap

<a href = "./django_project">- Day_17</a>        :   Django Simple Project
                    HTML inheritance
                    Many functions in blog/view.py
                    Form module
                    Log-in module

<a href = "./django_project">- Day_18</a>        :   Finish Django Simple Project 
                    Comment(model) inside of Post(model)
                    Change sqlite to MariaDB (Data in sqlite can't migrate)

<a href = "./ML">- Extra Class</a>      :   <a href= "./ML/iris_data.ipynb">Machine learning(Just basics) (iris data from sklearn)</a>
</pre>                 

## APIs
<pre>
<h4>Python open source list</h4>
1. Requests (Http client) <a href = 'https://requests.readthedocs.io/en/master/'>Documentation</a>
2. Beautifulsoup (Easier parsing! Easier than RE) <a href='https://www.crummy.com/software/BeautifulSoup/bs4/doc/'>Documentation</a>
3. Pandas (Table data processing, data analysis) <a href='https://pandas.pydata.org/'>Documentation</a>
4. Matplotlib (Visualizer, visualization) <a href='https://matplotlib.org/'>Documentation</a>
5. Seaborn (Easier than matplotlib, and more beautiful) <a href='https://seaborn.pydata.org/'>Documentation</a>
6. Pymysql (Mysql DB connector) <a href = 'https://pymysql.readthedocs.io/en/latest/' >Documentation</a>
7. Sqlalchemy (ORM: Object >> RDB) <a href='https://docs.sqlalchemy.org/en/13/'>Documentation</a>
    (
        Tabular data : DataFrame object
        ORM Rule :: 
        Class       <=>     Table
        Object      <=>     Row(Record)
        Variable    <=>     Column
    )
8-1. Pymongo (Mongodb driver) <a href= 'https://pymongo.readthedocs.io/en/stable/'>Documentation</a>
8-2. MongoDB <a href = 'https://docs.mongodb.com/manual/tutorial/getting-started/'>Tutorial</a> || <a href = 'https://docs.mongodb.com/drivers/pymongo'>Drivers</a>
9. Jupyter notebook (>> jupyter lab) <a href = "https://jupyter-notebook.readthedocs.io/en/stable/">Documentation</a> || <a href = "https://code.visualstudio.com/docs/python/jupyter-support">For_VScode</a>
10. Ajax (Q : What is the difference in Web between before and after the Ajax?)
  <a href = "./Practice/Day_9/congressman_scarping.ipynb"> >> Short explain</a>
</pre>


[NoSQL](https://tinyurl.com/y2zmhhx4) <br>
[Mongo DB](https://tinyurl.com/yxnsslgs) <br>
[Database shard](https://tinyurl.com/yyh64kck) <br>





