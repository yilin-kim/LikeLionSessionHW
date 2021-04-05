import requests
from bs4 import BeautifulSoup
import csv
from crawling_function import crawling

file = open('movie.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(['영화 제목','평점','이미지 주소','감독','출연자','개봉일자'])

MOVIE_URL ='https://movie.naver.com/movie/running/current.nhn'
movie_html = requests.get(MOVIE_URL)
movie_soup = BeautifulSoup(movie_html.text,'html.parser')

movie_list_box = movie_soup.find('ul', {'class':'lst_detail_t1'})
movie_list = movie_list_box.find_all('li')

final_result = crawling(movie_list)

for result in final_result :
    row =[]
    row.append(result['title'])
    row.append(result['rating'])
    row.append(result['img_src'])
    row.append(result['director'])
    row.append(result['actor'])
    row.append(result['date'])
    writer.writerow(row)