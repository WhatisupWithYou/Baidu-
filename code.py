import requests
import json

headers = {
    'Host':'zhaopin.baidu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}
def searchJob(job,city):
    base_url = 'https://zhaopin.baidu.com/quanzhi?query={}&city={}'.format(job,city)
    res=requests.get(base_url,headers=headers)
    # with open("2.txt","w",encoding="utf-8") as ff:
        # ff.write(res.text.encode('utf-8').decode('unicode_escape'))
        # ff.write(res.text)
    text=res.text
    start=text.find('data["list"]')
    end=text.find('"refresh_time":null}];')

    start_total=text.find('data["total"] = ')+17
    end_total=text.find('data["zpfr"]')-3
    total=text[start_total:end_total]

    data=text[start+15:end+21]
    try:
        datas=json.loads(data)
        print("地点：",city)
        print("职位总数：",total)

        for i in datas:
            title=i["title"]
            offical=i["officialname"]
            education=i["education"]
            experience=i["experience"]
            salary=i["salary"]
            types=i["type"]
            print("岗位：",title)
            print("公司:",offical)
            print("教育:",education)
            print("经验:",experience)
            print("薪资:",salary)
            print("类型:",types)
            input()
    except json.decoder.JSONDecodeError:
        print("请查找其它职位！")
if __name__=="__main__":
    city=input("请输入查找城市：")
    job=input("请输入查找职位：")
    searchJob(job,city)
