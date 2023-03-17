import json

str = """
{
    "code": 0,
    "result":
    {
        "pageResult":
        {
            "currentPage": 1,
            "pageSize": 100,
            "totalPage": 1,
            "total": 43,
            "data":
            [
                {
                    "user1Id": 64963,
                    "user2Id": 70782,
                    "totalNum": 84,
                    "totalVolume": "52139.469"
                },
                {
                    "user1Id": 64480,
                    "user2Id": 70782,
                    "totalNum": 42,
                    "totalVolume": "21442.258"
                },
                {
                    "user1Id": 64480,
                    "user2Id": 64528,
                    "totalNum": 21,
                    "totalVolume": "9525.397"
                },
                {
                    "user1Id": 64963,
                    "user2Id": 64965,
                    "totalNum": 16,
                    "totalVolume": "8265.3335"
                },
                {
                    "user1Id": 70782,
                    "user2Id": 70783,
                    "totalNum": 14,
                    "totalVolume": "6579.845"
                },
                {
                    "user1Id": 64498,
                    "user2Id": 64528,
                    "totalNum": 11,
                    "totalVolume": "2780.024"
                },
                {
                    "user1Id": 64498,
                    "user2Id": 64520,
                    "totalNum": 9,
                    "totalVolume": "1945.8613"
                },
                {
                    "user1Id": 51023,
                    "user2Id": 62451,
                    "totalNum": 8,
                    "totalVolume": "2704.5"
                },
                {
                    "user1Id": 51023,
                    "user2Id": 51023,
                    "totalNum": 7,
                    "totalVolume": "3660.173"
                },
                {
                    "user1Id": 51023,
                    "user2Id": 69758,
                    "totalNum": 4,
                    "totalVolume": "1189.864"
                },
                {
                    "user1Id": 51023,
                    "user2Id": 70806,
                    "totalNum": 4,
                    "totalVolume": "822.9386"
                },
                {
                    "user1Id": 51023,
                    "user2Id": 70430,
                    "totalNum": 4,
                    "totalVolume": "6426.7334"
                },
                {
                    "user1Id": 51023,
                    "user2Id": 70426,
                    "totalNum": 3,
                    "totalVolume": "9231.7424"
                },
                {
                    "user1Id": 51023,
                    "user2Id": 70165,
                    "totalNum": 3,
                    "totalVolume": "5016.4256"
                },
                {
                    "user1Id": 14791,
                    "user2Id": 51023,
                    "totalNum": 2,
                    "totalVolume": "1705.2156"
                },
                {
                    "user1Id": 51023,
                    "user2Id": 70425,
                    "totalNum": 2,
                    "totalVolume": "2107.2064"
                },
                {
                    "user1Id": 44379,
                    "user2Id": 51023,
                    "totalNum": 2,
                    "totalVolume": "431.76"
                },
                {
                    "user1Id": 64498,
                    "user2Id": 70165,
                    "totalNum": 2,
                    "totalVolume": "469.544"
                },
                {
                    "user1Id": 51023,
                    "user2Id": 70027,
                    "totalNum": 2,
                    "totalVolume": "2053.44"
                },
                {
                    "user1Id": 51023,
                    "user2Id": 70457,
                    "totalNum": 2,
                    "totalVolume": "733.92"
                },
                {
                    "user1Id": 51023,
                    "user2Id": 63609,
                    "totalNum": 2,
                    "totalVolume": "3285"
                },
                {
                    "user1Id": 40576,
                    "user2Id": 51023,
                    "totalNum": 1,
                    "totalVolume": "32.7414"
                },
                {
                    "user1Id": 51023,
                    "user2Id": 70782,
                    "totalNum": 1,
                    "totalVolume": "505.578"
                },
                {
                    "user1Id": 51023,
                    "user2Id": 61802,
                    "totalNum": 1,
                    "totalVolume": "289.98"
                },
                {
                    "user1Id": 63503,
                    "user2Id": 70782,
                    "totalNum": 1,
                    "totalVolume": "8140.736"
                },
                {
                    "user1Id": 51023,
                    "user2Id": 64036,
                    "totalNum": 1,
                    "totalVolume": "1105.8052"
                },
                {
                    "user1Id": 51023,
                    "user2Id": 70009,
                    "totalNum": 1,
                    "totalVolume": "2523.42"
                },
                {
                    "user1Id": 70877,
                    "user2Id": 70877,
                    "totalNum": 1,
                    "totalVolume": "34.3047"
                },
                {
                    "user1Id": 15248,
                    "user2Id": 56609,
                    "totalNum": 1,
                    "totalVolume": "215.1359462"
                },
                {
                    "user1Id": 51023,
                    "user2Id": 64480,
                    "totalNum": 1,
                    "totalVolume": "465.212"
                },
                {
                    "user1Id": 53535,
                    "user2Id": 70226,
                    "totalNum": 1,
                    "totalVolume": "4361.4"
                },
                {
                    "user1Id": 51023,
                    "user2Id": 62811,
                    "totalNum": 1,
                    "totalVolume": "1046.374"
                },
                {
                    "user1Id": 23724,
                    "user2Id": 63005,
                    "totalNum": 1,
                    "totalVolume": "18.55524352"
                },
                {
                    "user1Id": 51023,
                    "user2Id": 64920,
                    "totalNum": 1,
                    "totalVolume": "1207.68"
                },
                {
                    "user1Id": 51023,
                    "user2Id": 52891,
                    "totalNum": 1,
                    "totalVolume": "155.334"
                },
                {
                    "user1Id": 61544,
                    "user2Id": 61544,
                    "totalNum": 1,
                    "totalVolume": "2416.691756"
                },
                {
                    "user1Id": 51023,
                    "user2Id": 70126,
                    "totalNum": 1,
                    "totalVolume": "784.416"
                },
                {
                    "user1Id": 51023,
                    "user2Id": 63024,
                    "totalNum": 1,
                    "totalVolume": "511.2"
                },
                {
                    "user1Id": 30053,
                    "user2Id": 64639,
                    "totalNum": 1,
                    "totalVolume": "41.503"
                },
                {
                    "user1Id": 51023,
                    "user2Id": 69427,
                    "totalNum": 1,
                    "totalVolume": "1516.95"
                },
                {
                    "user1Id": 51023,
                    "user2Id": 60844,
                    "totalNum": 1,
                    "totalVolume": "65.192"
                },
                {
                    "user1Id": 70061,
                    "user2Id": 70165,
                    "totalNum": 1,
                    "totalVolume": "1007.8684"
                },
                {
                    "user1Id": 62471,
                    "user2Id": 63024,
                    "totalNum": 1,
                    "totalVolume": "337.9"
                }
            ]
        }
    }
}
"""


s = """
{
      "doc_count_error_upper_bound" : 0,
      "sum_other_doc_count" : 0,
      "buckets" : [
        {
          "key" : "DFG-USDT-SPOT",
          "doc_count" : 477,
          "totalSell" : {
            "value" : 2282.0
          },
          "totalBuyUsdt" : {
            "value" : 12445.3098059
          },
          "totalSellUsdt" : {
            "value" : 10171.2616257
          },
          "totalBuy" : {
            "value" : 2761.1
          }
        },
        {
          "key" : "GRV-USDT-SPOT",
          "doc_count" : 83,
          "totalSell" : {
            "value" : 7097.08
          },
          "totalBuyUsdt" : {
            "value" : 0.0
          },
          "totalSellUsdt" : {
            "value" : 5205.7700501
          },
          "totalBuy" : {
            "value" : 0.0
          }
        },
        {
          "key" : "BTC-USDT-SPOT",
          "doc_count" : 33,
          "totalSell" : {
            "value" : 3.48685
          },
          "totalBuyUsdt" : {
            "value" : 39575.910554430004
          },
          "totalSellUsdt" : {
            "value" : 70618.64652019
          },
          "totalBuy" : {
            "value" : 1.96291
          }
        },
        {
          "key" : "HAM-USDT-SPOT",
          "doc_count" : 22,
          "totalSell" : {
            "value" : 5.7254858156E10
          },
          "totalBuyUsdt" : {
            "value" : 101.7383919312191
          },
          "totalSellUsdt" : {
            "value" : 200.78927108212721
          },
          "totalBuy" : {
            "value" : 3.0321481509E10
          }
        },
        {
          "key" : "APE-USDT-SPOT",
          "doc_count" : 20,
          "totalSell" : {
            "value" : 64.5014
          },
          "totalBuyUsdt" : {
            "value" : 229.76391289
          },
          "totalSellUsdt" : {
            "value" : 249.00990793000003
          },
          "totalBuy" : {
            "value" : 59.9176
          }
        },
        {
          "key" : "INJ-USDT-SPOT",
          "doc_count" : 17,
          "totalSell" : {
            "value" : 1118.1000000000001
          },
          "totalBuyUsdt" : {
            "value" : 3125.5384
          },
          "totalSellUsdt" : {
            "value" : 3531.2997
          },
          "totalBuy" : {
            "value" : 982.1
          }
        },
        {
          "key" : "JASMY-USDT-SPOT",
          "doc_count" : 13,
          "totalSell" : {
            "value" : 111347.5
          },
          "totalBuyUsdt" : {
            "value" : 0.0
          },
          "totalSellUsdt" : {
            "value" : 535.4190381999999
          },
          "totalBuy" : {
            "value" : 0.0
          }
        },
        {
          "key" : "ADP-USDT-SPOT",
          "doc_count" : 10,
          "totalSell" : {
            "value" : 4556.46
          },
          "totalBuyUsdt" : {
            "value" : 0.0
          },
          "totalSellUsdt" : {
            "value" : 33.7633686
          },
          "totalBuy" : {
            "value" : 0.0
          }
        },
        {
          "key" : "DAR-USDT-SPOT",
          "doc_count" : 10,
          "totalSell" : {
            "value" : 5411.0
          },
          "totalBuyUsdt" : {
            "value" : 121.5884
          },
          "totalSellUsdt" : {
            "value" : 835.77062
          },
          "totalBuy" : {
            "value" : 788.0
          }
        },
        {
          "key" : "APT-USDT-SPOT",
          "doc_count" : 9,
          "totalSell" : {
            "value" : 110.50999999999999
          },
          "totalBuyUsdt" : {
            "value" : 2041.730683
          },
          "totalSellUsdt" : {
            "value" : 1150.961957
          },
          "totalBuy" : {
            "value" : 196.84
          }
        },
        {
          "key" : "POKT-USDT-SPOT",
          "doc_count" : 6,
          "totalSell" : {
            "value" : 0.0
          },
          "totalBuyUsdt" : {
            "value" : 3217.695216
          },
          "totalSellUsdt" : {
            "value" : 0.0
          },
          "totalBuy" : {
            "value" : 59786.535
          }
        },
        {
          "key" : "ENS-USDT-SPOT",
          "doc_count" : 5,
          "totalSell" : {
            "value" : 10.22
          },
          "totalBuyUsdt" : {
            "value" : 0.0
          },
          "totalSellUsdt" : {
            "value" : 123.8385169
          },
          "totalBuy" : {
            "value" : 0.0
          }
        },
        {
          "key" : "ETH-USDT-SPOT",
          "doc_count" : 5,
          "totalSell" : {
            "value" : 3.60256
          },
          "totalBuyUsdt" : {
            "value" : 8052.724291179999
          },
          "totalSellUsdt" : {
            "value" : 5254.533014480001
          },
          "totalBuy" : {
            "value" : 5.52916
          }
        },
        {
          "key" : "GLEEC-USDT-SPOT",
          "doc_count" : 5,
          "totalSell" : {
            "value" : 2354.0
          },
          "totalBuyUsdt" : {
            "value" : 289.596428
          },
          "totalSellUsdt" : {
            "value" : 118.266896
          },
          "totalBuy" : {
            "value" : 6307.0
          }
        },
        {
          "key" : "GMT-USDT-SPOT",
          "doc_count" : 5,
          "totalSell" : {
            "value" : 315.5
          },
          "totalBuyUsdt" : {
            "value" : 93.72012000000001
          },
          "totalSellUsdt" : {
            "value" : 94.968655
          },
          "totalBuy" : {
            "value" : 312.0
          }
        },
        {
          "key" : "FXS-USDT-SPOT",
          "doc_count" : 4,
          "totalSell" : {
            "value" : 9.2
          },
          "totalBuyUsdt" : {
            "value" : 19.6872
          },
          "totalSellUsdt" : {
            "value" : 69.36160000000001
          },
          "totalBuy" : {
            "value" : 2.6
          }
        },
        {
          "key" : "GALA-USDT-SPOT",
          "doc_count" : 4,
          "totalSell" : {
            "value" : 14781.0
          },
          "totalBuyUsdt" : {
            "value" : 165.82716
          },
          "totalSellUsdt" : {
            "value" : 454.66341
          },
          "totalBuy" : {
            "value" : 5391.0
          }
        },
        {
          "key" : "GMMT-USDT-SPOT",
          "doc_count" : 2,
          "totalSell" : {
            "value" : 0.0
          },
          "totalBuyUsdt" : {
            "value" : 632.959413
          },
          "totalSellUsdt" : {
            "value" : 0.0
          },
          "totalBuy" : {
            "value" : 246.97
          }
        },
        {
          "key" : "HIGH-USDT-SPOT",
          "doc_count" : 2,
          "totalSell" : {
            "value" : 68.784
          },
          "totalBuyUsdt" : {
            "value" : 0.0
          },
          "totalSellUsdt" : {
            "value" : 124.42811999999999
          },
          "totalBuy" : {
            "value" : 0.0
          }
        },
        {
          "key" : "LOKA-USDT-SPOT",
          "doc_count" : 2,
          "totalSell" : {
            "value" : 388.71299999999997
          },
          "totalBuyUsdt" : {
            "value" : 0.0
          },
          "totalSellUsdt" : {
            "value" : 165.16415369999999
          },
          "totalBuy" : {
            "value" : 0.0
          }
        },
        {
          "key" : "RBN-USDT-SPOT",
          "doc_count" : 2,
          "totalSell" : {
            "value" : 191.612
          },
          "totalBuyUsdt" : {
            "value" : 0.0
          },
          "totalSellUsdt" : {
            "value" : 37.1729482
          },
          "totalBuy" : {
            "value" : 0.0
          }
        },
        {
          "key" : "THE-USDT-SPOT",
          "doc_count" : 2,
          "totalSell" : {
            "value" : 5620.2
          },
          "totalBuyUsdt" : {
            "value" : 0.0
          },
          "totalSellUsdt" : {
            "value" : 11.602958000000001
          },
          "totalBuy" : {
            "value" : 0.0
          }
        },
        {
          "key" : "TSUKA-USDT-SPOT",
          "doc_count" : 2,
          "totalSell" : {
            "value" : 4478.700000000001
          },
          "totalBuyUsdt" : {
            "value" : 0.0
          },
          "totalSellUsdt" : {
            "value" : 331.6947768
          },
          "totalBuy" : {
            "value" : 0.0
          }
        },
        {
          "key" : "USTC-USDT-SPOT",
          "doc_count" : 2,
          "totalSell" : {
            "value" : 6924.0
          },
          "totalBuyUsdt" : {
            "value" : 0.0
          },
          "totalSellUsdt" : {
            "value" : 151.25778617
          },
          "totalBuy" : {
            "value" : 0.0
          }
        },
        {
          "key" : "WOO-USDT-SPOT",
          "doc_count" : 2,
          "totalSell" : {
            "value" : 267.65
          },
          "totalBuyUsdt" : {
            "value" : 18.582677999999998
          },
          "totalSellUsdt" : {
            "value" : 44.681490999999994
          },
          "totalBuy" : {
            "value" : 112.52
          }
        },
        {
          "key" : "BTRST-USDT-SPOT",
          "doc_count" : 1,
          "totalSell" : {
            "value" : 39.507
          },
          "totalBuyUsdt" : {
            "value" : 0.0
          },
          "totalSellUsdt" : {
            "value" : 32.158697999999994
          },
          "totalBuy" : {
            "value" : 0.0
          }
        },
        {
          "key" : "BTT-USDT-SPOT",
          "doc_count" : 1,
          "totalSell" : {
            "value" : 1.4417418E7
          },
          "totalBuyUsdt" : {
            "value" : 0.0
          },
          "totalSellUsdt" : {
            "value" : 8.93879916
          },
          "totalBuy" : {
            "value" : 0.0
          }
        },
        {
          "key" : "EL-USDT-SPOT",
          "doc_count" : 1,
          "totalSell" : {
            "value" : 139277.01
          },
          "totalBuyUsdt" : {
            "value" : 0.0
          },
          "totalSellUsdt" : {
            "value" : 357.9419157
          },
          "totalBuy" : {
            "value" : 0.0
          }
        },
        {
          "key" : "LUNA-USDT-SPOT",
          "doc_count" : 1,
          "totalSell" : {
            "value" : 2.83
          },
          "totalBuyUsdt" : {
            "value" : 0.0
          },
          "totalSellUsdt" : {
            "value" : 3.606269
          },
          "totalBuy" : {
            "value" : 0.0
          }
        },
        {
          "key" : "MASK-USDT-SPOT",
          "doc_count" : 1,
          "totalSell" : {
            "value" : 62.02
          },
          "totalBuyUsdt" : {
            "value" : 0.0
          },
          "totalSellUsdt" : {
            "value" : 172.91176
          },
          "totalBuy" : {
            "value" : 0.0
          }
        },
        {
          "key" : "SAND-USDT-SPOT",
          "doc_count" : 1,
          "totalSell" : {
            "value" : 0.0
          },
          "totalBuyUsdt" : {
            "value" : 87.9422
          },
          "totalSellUsdt" : {
            "value" : 0.0
          },
          "totalBuy" : {
            "value" : 167.0
          }
        },
        {
          "key" : "SUKU-USDT-SPOT",
          "doc_count" : 1,
          "totalSell" : {
            "value" : 53.617
          },
          "totalBuyUsdt" : {
            "value" : 0.0
          },
          "totalSellUsdt" : {
            "value" : 3.8389771999999995
          },
          "totalBuy" : {
            "value" : 0.0
          }
        },
        {
          "key" : "XEN-USDT-SPOT",
          "doc_count" : 1,
          "totalSell" : {
            "value" : 0.0
          },
          "totalBuyUsdt" : {
            "value" : 3.578777400252582
          },
          "totalSellUsdt" : {
            "value" : 0.0
          },
          "totalBuy" : {
            "value" : 5262907.94
          }
        }
      ]
    }
"""
js = json.loads(s)
buckets = js.get('buckets')

for bucket in buckets:
    symbol = bucket.get('key')
    cou = bucket.get('doc_count')
    totalSell = bucket.get('totalSell').get('value')
    totalSellUsdt = bucket.get('totalSellUsdt').get('value')
    avgSell = totalSellUsdt / totalSell if totalSell > 0 else 0
    totalBuy = bucket.get('totalBuy').get('value')
    totalBuyUsdt = bucket.get('totalBuyUsdt').get('value')
    avgBuy = totalBuyUsdt / totalBuy if totalBuy > 0 else 0
    # print(f'symbol:{symbol}\tcount:{cou}\tbuy:{totalBuy}\tsell:{totalSell}' )
    print(f'{symbol}\t{cou}\t{totalBuy}\t{avgBuy}\t{totalBuyUsdt}\t{totalSell}\t{avgSell}\t{totalSellUsdt}' )

