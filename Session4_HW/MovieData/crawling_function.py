def crawling(movie_list):
    final_result = []
    for movie in movie_list:
        title = movie.find('dt',{'class':'tit'}).find('a').text
        rating = movie.find('div',{'class':'star_t1'}).find('span',{'class':'num'}).text
        img_src = movie.find('div',{'class':'thumb'}).find('img')['src']
        director = movie.find()
        actor = 'None'
        actors = movie.find('d1',{'class':'info_txt1'}).find_all('dd')
        if len(actors) >= 3:
            actors_list = actors[2].find_all('a')
            actor =[]
            for actor_list in actors_list:
                actor.append(actor_list.text)
        date = movie.find('d1', {'class','info_txt1'}).find('dd').contents[6].strip()

        movie_info = {
            'title': title,
            'rating':rating,
            'img_src': img_src,
            'director': director,
            'actor': actor,
            'date':date
        }
        final_result.append(movie_info)

    return final_result
