import requests
from datetime import datetime
TOKEN="john@1234"
USERNAME="johnmisquitta"
END_POINT=" https://pixe.la/v1/users"
parameters={
    "token":TOKEN ,
    "username":USERNAME ,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
    "thanksCode":"ThisIsThanksCode"

}
#create a user
# response=requests.post(url=END_POINT,json=parameters)
# print(response.text)



# create_graph_param={
#
#     "id":"graph1",
#     "name":"book_pages",
#     "unit":"pg",
#     "type":"int",
#     "color":"sora"
# }
# header_param={
#     'X-USER-TOKEN':TOKEN
#
# }
# graph_endpoint=f"{END_POINT}/{USERNAME}/graphs"
# response=requests.post(url=graph_endpoint,json=create_graph_param,headers=header_param)
# print(response.text)

#create a pixel
# date=datetime.now()
# today=date.strftime("%Y%m%d")
# # today=datetime(year=2023,month=2,day=6)
# print(today)
# create_pixel_param={
# "date": today,"quantity":"4","optionalData":"{\"key\":\"value\"}"
# }
# header_param={
#     'X-USER-TOKEN':TOKEN
#  }
# graph_endpoint=f"{END_POINT}/{USERNAME}/graphs/graph1"
# response=requests.post(url=graph_endpoint,json=create_pixel_param,headers=header_param)
# print(response.text)

#show stats
graph_endpoint=f"{END_POINT}/{USERNAME}/graphs/graph1/stats"
response=requests.get(url=graph_endpoint)

print(response.text)



#update a pixel
date=datetime.now()
today=date.strftime("%Y%m%d")
#today=datetime(year=2023,month=2,day=6)

create_pixel_param={
"quantity":"7","optionalData":"{\"key\":\"value\"}"
}
header_param={
    'X-USER-TOKEN':TOKEN
 }
graph_endpoint=f"{END_POINT}/{USERNAME}/graphs/graph1/{today}"
response=requests.put(url=graph_endpoint,json=create_pixel_param,headers=header_param)
print(response.text)