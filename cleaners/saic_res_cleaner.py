import json
import cloudscraper
from bs4 import BeautifulSoup

ids=[]
clean=["https://digitalcollections.saic.edu/islandora/object/islandora%3A16735",
"https://digitalcollections.saic.edu/islandora/object/islandora%3A16804",
"https://digitalcollections.saic.edu/islandora/object/islandora%3A16814",
"https://digitalcollections.saic.edu/islandora/object/islandora%3A16827",
"https://digitalcollections.saic.edu/islandora/object/islandora%3A16842",
"https://digitalcollections.saic.edu/islandora/object/islandora%3A44268",
"https://digitalcollections.saic.edu/islandora/object/islandora%3A44304",
"https://digitalcollections.saic.edu/islandora/object/islandora%3A44315",
"https://digitalcollections.saic.edu/islandora/object/islandora%3A44338",
"https://digitalcollections.saic.edu/islandora/object/islandora%3A44359",
"https://digitalcollections.saic.edu/islandora/object/islandora%3A44456",
"https://digitalcollections.saic.edu/islandora/object/islandora%3A44459",
"https://digitalcollections.saic.edu/islandora/object/islandora%3A44463",
"https://digitalcollections.saic.edu/islandora/object/islandora%3A44476",
"https://digitalcollections.saic.edu/islandora/object/islandora%3A44501",
"https://digitalcollections.saic.edu/islandora/object/islandora%3A44658",
"https://digitalcollections.saic.edu/islandora/object/islandora%3A44704",
"https://digitalcollections.saic.edu/islandora/object/islandora%3A44710",
"https://digitalcollections.saic.edu/islandora/object/islandora%3A44713",
"https://digitalcollections.saic.edu/islandora/object/islandora%3A44716",
"https://digitalcollections.saic.edu/islandora/object/islandora%3A44722",
"https://digitalcollections.saic.edu/islandora/object/islandora%3A44742",
"https://digitalcollections.saic.edu/islandora/object/islandora%3A44745",
"https://digitalcollections.saic.edu/islandora/object/islandora%3A44748",
"https://digitalcollections.saic.edu/islandora/object/islandora%3A44751",
"https://digitalcollections.saic.edu/islandora/object/islandora%3A44755",
"https://digitalcollections.saic.edu/islandora/object/islandora%3A44758",
"https://digitalcollections.saic.edu/islandora/object/islandora%3A44771",
"https://digitalcollections.saic.edu/islandora/object/islandora%3A44812",
"https://digitalcollections.saic.edu/islandora/object/islandora%3A44876",
"https://digitalcollections.saic.edu/islandora/object/islandora%3A45006",
"https://digitalcollections.saic.edu/islandora/object/islandora%3A45022",
"https://digitalcollections.saic.edu/islandora/object/islandora%3A45028",
"https://digitalcollections.saic.edu/islandora/object/islandora%3A45032",
"https://digitalcollections.saic.edu/islandora/object/islandora%3A45041",
"https://digitalcollections.saic.edu/islandora/object/islandora%3A45067",
"https://digitalcollections.saic.edu/islandora/object/islandora%3A45080",
"https://digitalcollections.saic.edu/islandora/object/islandora%3A45087",
"https://digitalcollections.saic.edu/islandora/object/islandora%3A45094",
"https://digitalcollections.saic.edu/islandora/object/islandora%3A45147",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_10057",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_10089",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_10104",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_10128",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_10136",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_10151",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_10164",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_10171",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_10184",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_10239",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_10250",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_10265",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_10305",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_10316",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_10341",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_10408",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_10423",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_10441",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_10476",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_10499",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_10506",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_10512",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_10556",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_10559",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_10621",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_10774",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_10777",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_10812",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_10870",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_10875",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_10884",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_10923",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_10935",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_10950",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_10957",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_1100",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_11098",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_11124",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_11138",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_11170",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_11241",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_11294",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_11303",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_11378",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_11392",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_11444",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_11458",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_11508",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_11537",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_11563",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_1161",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_11700",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_11703",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_11722",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_11755",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_11762",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_11765",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_11794",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_11797",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_11812",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_11816",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_11898",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_11980",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_11983",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_12000",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_12012",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_1229",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_1262",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_1686",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_1729",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_1865",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_2018",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_2039",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_2052",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_2055",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_2061",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_2083",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_2106",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_2114",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_2123",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_2186",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_2252",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_2283",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_2294",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_2336",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_2371",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_2448",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_2479",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_2566",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_2574",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_2588",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_2625",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_2701",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_2719",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_2761",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_2820",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_2908",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_2918",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_2931",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_2939",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_2964",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_3577",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_3854",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_3872",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_3914",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_4082",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_427",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_4272",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_444",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_4467",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_4700",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_4753",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_4835",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_4899",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_4927",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_4947",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_4953",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_5019",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_5082",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_5206",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_5217",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_5261",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_5264",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_5276",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_5357",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_5365",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_5368",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_5429",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_5470",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_5473",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_5513",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_5562",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_5682",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_5812",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_5832",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_5956",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_6120",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_6123",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_6232",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_6378",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_6441",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_6517",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_6572",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_6612",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_6618",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_6743",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_6820",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_6933",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_6938",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_6963",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_6972",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_7038",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_7042",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_7212",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_7219",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_7253",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_7271",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_7347",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_7422",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_749",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_7530",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_7542",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_7627",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_7645",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_7665",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_768",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_7723",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_7794",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_806",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_8626",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_8837",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_8879",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_8885",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_8888",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_8928",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_8971",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9023",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9026",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9067",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9096",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9104",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9110",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9118",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9149",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9156",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9257",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9272",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9290",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9299",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9309",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9334",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9342",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9352",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9368",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9414",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9429",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9435",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9499",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9518",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9532",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9535",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9556",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9637",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_964",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9651",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9657",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9700",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9725",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9746",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9770",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9803",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9811",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9832",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9838",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9849",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9866",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9877",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9883",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9895",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9912",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9962",
"https://digitalcollections.saic.edu/islandora/object/islandora%3Acorrespondence_9970"]


#get IDs of mail art to delete from results
for link in clean:
    scraper = cloudscraper.create_scraper()
    work_url = link
    page = scraper.get(work_url)
    soup2 = BeautifulSoup(page.text, 'html.parser')

    number_info = soup2.find('span',{'class': 'views-field views-field-field-local-identifier'})
    id_num = number_info.find('span',{'class':'field-content'}).text.strip()
    ids.append(id_num)
print("done")

with open("ids_delete", "w") as failed_ids:
    json.dump(ids, failed_ids,indent = 2)
print("all done")



