# Gitee_OPENAPI
基于Gitee官方OPEN API编写

[Gitee官方OPEN API](https://gitee.com/api/v5/swagger#/getV5ReposOwnerRepoStargazers?ex=no)

# DEMO
```
if __name__ == '__main__':
    token = 'token'
    gists_id = '3o9schx4a6vftlmz1ydbr46'

    gitee = giteeCodeSnippet(token, gists_id)

    # 初始化gists,适合第一次在没有gists_id情况下使用
    # print(gitee.addNewGists('sync app data'))
    # print('=' * 50)

    # 获取所有gists_id
    # print(gitee.getGists())
    # print('=' * 50)

    # 修改指定gists_id的内容
    # data1 = {"lastSyncTime": 1664290361871, "electermVersion": "1.23.1"}
    # data2 = [{"id": "defaul", "title1": "default", "bookmarkIds": ["5fV2YSa", "T_m9m_7", "DlvM4Q_", "k5MMgfw", "ZZd1VsL"], "bookmarkGroupIds": []}]
    # data3 = {}
    # data4 = [1, 2, 3, 4, 5]
    # # yapf: disable
    # print(gitee.setGists('sync app data', {
    #             'userConfig.json': {
    #                 'content': json.dumps(data1)
    #                 },
    #             'b.json': {
    #                 'content': json.dumps(data2)
    #             },
    #             'test.json': {
    #                 'content': json.dumps(data3)
    #             },
    #             'list.json': {
    #                 'content': json.dumps(data4)
    #             }
    #         }
    #     )
    # )
    # # yapf: enable
    # print('=' * 50)

    # 获取所有description和gists_id
    # print(gitee.getAllGistsID())
    # try:
    #     print(gitee.getAllGistsID()['sync app data'])
    # except KeyError:
    #     print('不存在!')

    # try:
    #     print(gitee.getAllGistsID()['sync app data1'])
    # except KeyError:
    #     print('不存在!')
    # print('=' * 50)

    # 删除指定gists_id
    # print(gitee.delGists())
    # print('=' * 50)
```
