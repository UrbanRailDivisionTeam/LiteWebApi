from pymongo import MongoClient

connect = MongoClient(host="localhost", port=27017)


def main():
    db = connect['liteweb']
    coll_0 = db['calibration_line_total_data']
    coll_0.drop()
    coll_0.insert_many([
        {
            "index": 0,
            "title_name": "未响应异常数",
            "trend": "overtime",
            "request_value": 12,
            "request_time": 120,
            "average_time": 203.86128747795414
        },
        {
            "title_name": "一次诊断进行中流程数",
            "index": 1,
            "trend": "overtime",
            "request_value": 0,
            "request_time": 120,
            "average_time": 2067.414374999999
        },
        {
            "index": 2,
            "title_name": "二次诊断进行中流程数",
            "trend": "ontime",
            "request_value": 28,
            "request_time": 120,
            "average_time": 119.9724358974359
        },
        {
            "index": 3,
            "title_name": "返工进行中流程数",
            "trend": "ontime",
            "request_value": 0,
            "request_time": 120,
            "average_time": 0
        },
        {
            "index": 4,
            "title_name": "验收进行中流程数",
            "trend": "ontime",
            "request_value": 0,
            "request_time": 120,
            "average_time": 0
        }
    ])

    coll_1 = db['calibration_line_group_data']
    coll_1.drop()
    coll_1.insert_many([
        {
            "index": 0,
            "title_name": "异常响应及时率",
            "trend": "overlimit",
            "group": [
                {
                    "group_name": "内装三工位",
                    "ontime_value": 2,
                    "total_value": 3
                },
                {
                    "group_name": "电气工程设计组",
                    "ontime_value": 0,
                    "total_value": 3
                },
                {
                    "group_name": "调试组",
                    "ontime_value": 19,
                    "total_value": 19
                },
                {
                    "group_name": "电工四工位",
                    "ontime_value": 38,
                    "total_value": 54
                },
                {
                    "group_name": "电工三工位",
                    "ontime_value": 36,
                    "total_value": 41
                },
                {
                    "group_name": "校线一班",
                    "ontime_value": 0,
                    "total_value": 3
                },
                {
                    "group_name": "质量保证组",
                    "ontime_value": 7,
                    "total_value": 7
                },
                {
                    "group_name": "精益信息化组",
                    "ontime_value": 2,
                    "total_value": 2
                },
                {
                    "group_name": "校线二班",
                    "ontime_value": 0,
                    "total_value": 6
                },
                {
                    "group_name": "内装一工位",
                    "ontime_value": 2,
                    "total_value": 2
                },
                {
                    "group_name": "电工一工位",
                    "ontime_value": 36,
                    "total_value": 61
                }
            ]
        },
        {
            "index": 1,
            "title_name": "一次诊断及时率",
            "trend": "overlimit",
            "group": [
                {
                    "group_name": "校线二班",
                    "ontime_value": 5,
                    "total_value": 37
                },
                {
                    "group_name": "校线一班",
                    "ontime_value": 2,
                    "total_value": 43
                }
            ]
        },
        {
            "index": 2,
            "title_name": "二次诊断及时率",
            "trend": "overlimit",
            "group": [
                {
                    "group_name": "电气工程设计组",
                    "ontime_value": 0,
                    "total_value": 4
                },
                {
                    "group_name": "总成进程组",
                    "ontime_value": 0,
                    "total_value": 19
                },
                {
                    "group_name": "调试组",
                    "ontime_value": 3,
                    "total_value": 3
                },
                {
                    "group_name": "质量保证组",
                    "ontime_value": 1,
                    "total_value": 1
                },
                {
                    "group_name": "电工三工位",
                    "ontime_value": 6,
                    "total_value": 12
                },
                {
                    "group_name": "校线一班",
                    "ontime_value": 10,
                    "total_value": 10
                },
                {
                    "group_name": "电工四工位",
                    "ontime_value": 4,
                    "total_value": 5
                },
                {
                    "group_name": "电气组",
                    "ontime_value": 2,
                    "total_value": 2
                },
                {
                    "group_name": "电工一工位",
                    "ontime_value": 20,
                    "total_value": 24
                }
            ]
        },
        {
            "index": 3,
            "title_name": "返工及时率",
            "trend": "inlimit",
            "group": [
                {
                    "group_name": "校线二班",
                    "ontime_value": 13,
                    "total_value": 13
                },
                {
                    "group_name": "校线一班",
                    "ontime_value": 39,
                    "total_value": 39
                }
            ]
        },
        {
            "index": 4,
            "title_name": "验收及时率",
            "trend": "inlimit",
            "group": [
                {
                    "group_name": "校线二班",
                    "ontime_value": 13,
                    "total_value": 13
                },
                {
                    "group_name": "校线一班",
                    "ontime_value": 39,
                    "total_value": 39
                }
            ]
        }
    ])

    coll_2 = db['pie_chart_error_data']
    coll_2.drop()
    coll_2.insert_many([
        {
            "index": 0,
            "title_name": "异常原因整体组成",
            "data": [
                {
                    "label": "来料",
                    "value": 1
                },
                {
                    "label": "工艺",
                    "value": 2
                },
                {
                    "label": "下线",
                    "value": 7
                },
                {
                    "label": "布线",
                    "value": 7
                },
                {
                    "label": "接线",
                    "value": 7
                },
                {
                    "label": "计划下达",
                    "value": 7
                },
                {
                    "label": "后续工序",
                    "value": 7
                },
                {
                    "label": "变更执行",
                    "value": 7
                },
            ]
        },
        {
            "index": 0,
            "title_name": "来料导致的异常",
            "data": [
                {
                    "label": "松动",
                    "value": 1
                },
                {
                    "label": "漏导体",
                    "value": 2
                },
                {
                    "label": "断裂",
                    "value": 1
                },
                {
                    "label": "接口失配",
                    "value": 6
                },
            ]
        },
        {
            "index": 0,
            "title_name": "下线导致的异常",
            "data": []
        },
        {
            "index": 0,
            "title_name": "接线导致的异常",
            "data": []
        },
        {
            "index": 0,
            "title_name": "布线导致的异常",
            "data": []
        },
        {
            "index": 0,
            "title_name": "计划下达导致的异常",
            "data": []
        },
        {
            "index": 0,
            "title_name": "后续工序导致的异常",
            "data": []
        },
        {
            "index": 0,
            "title_name": "变更执行导致的异常",
            "data": []
        },
        {
            "index": 0,
            "title_name": "工艺导致的异常",
            "data": []
        },
        {
            "index": 0,
            "title_name": "设计导致的异常",
            "data": []
        }
    ])

    coll_3 = db['pie_chart_no_error_data']
    coll_3.drop()
    coll_3.insert_many([
        {
            "index": 0,
            "title_name": "本月异常构型组成",
            "data": [
                {
                    "label": "线号",
                    "value": 12
                },
                {
                    "label": " ",
                    "value": 60
                },
                {
                    "label": "终端",
                    "value": 51
                },
                {
                    "label": "插芯",
                    "value": 10
                },
                {
                    "label": "标签",
                    "value": 26
                },
                {
                    "label": "电缆",
                    "value": 28
                },
                {
                    "label": "扎带",
                    "value": 1
                }
            ]
        },
        {
            "index": 1,
            "title_name": "本月异常项目占比",
            "data": [
                {
                    "label": "SML1EXP4G",
                    "value": 1
                },
                {
                    "label": "MMLRVS2",
                    "value": 68
                },
                {
                    "label": "CSL6",
                    "value": 1
                },
                {
                    "label": "SML18EXP",
                    "value": 131
                }
            ]
        },
        {
            "index": 2,
            "title_name": "本月异常责任单位占比",
            "data": [
                {
                    "label": "制造班组",
                    "value": 57
                },
                {
                    "label": " ",
                    "value": 60
                },
                {
                    "label": "供应商",
                    "value": 10
                },
                {
                    "label": "机车事业部管线班",
                    "value": 10
                },
                {
                    "label": "电气工艺",
                    "value": 15
                },
                {
                    "label": "物流",
                    "value": 2
                },
                {
                    "label": "默认",
                    "value": 4
                },
                {
                    "label": "项目工程部",
                    "value": 2
                },
                {
                    "label": "无",
                    "value": 2
                },
                {
                    "label": "项目",
                    "value": 4
                },
                {
                    "label": "设计",
                    "value": 22
                }
            ]
        }
    ])

    coll_4 = db['update_time']
    coll_4.drop()
    coll_4.insert_many([
        {
            'name': 'calibration_line',
            'time': '2025-04-25 15:25:28'
        },
    ])


if __name__ == '__main__':
    main()
