import requests
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}
url = 'https://www.zhihu.com/api/v4/people/fcc808ca04188e8fbfebd590592583ec/collections?include=data%5B*%5D.updated_time%2Canswer_count%2Cfollower_count%2Ccreator%2Cdescription%2Cis_following%2Ccomment_count%2Ccreated_time%3Bdata%5B*%5D.creator.vip_info&offset=0&limit=10'

# 获取收藏夹的id 和 收藏夹名。想打开收藏夹需要收藏夹的id
favoriteId = []
def getFavoriteId():
    r = requests.get(url,headers=headers).json()
    for i in range(0,len(r['data'])):
        id = r['data'][i]['id']
        title = r['data'][i]['title']
        temp = [
            id,
            title
        ]
        favoriteId.append(temp)
# 根据获取到的收藏夹的id生成打开收藏夹的链接
favoriteLinks = []
def getLink():
    for i in range(0,len(favoriteId)):
        url = 'https://www.zhihu.com/api/v4/collections/'+str(favoriteId[i][0])+'/items?offset=0&limit=20'
        favoriteLinks.append(url)

# 解析收藏夹链接里面的内容，提取出内容标题和内容链接
def getConent(favoriteLink):
    r = requests.get(favoriteLink,headers=headers).json()
    for i in range(0,len(r['data'])):
        em =r['data'][i]
        result = str(em['content']['question']['title']) + str( em['content']['question']['url'])
        print(result)

if __name__ == '__main__':
    getFavoriteId()
    getLink()
    for i in range(0,len(favoriteLinks)):
        print(favoriteId[i][1]+'************************************************************************************************************************')
        getConent(favoriteLinks[i])


        

