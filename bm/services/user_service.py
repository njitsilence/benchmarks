from django.conf import settings
import requests


# 批量获取用户详情
def batch_get_user_info(user_id):
    user_id_dict = {}
    user_id_dict['users'] = list(user_id)
    url = settings.BATCH_GET_USER_INFO_URL
    resp = requests.post(url,json=user_id_dict)
    user = []
    resp=resp.json()
    if resp and resp['result'] is not None:
        for item in resp['result']:
            user.append(item)
        return user
    elif not resp['result']:
        return []
    return None


def batch_get_user_info_list(user_id_list):
    # 调用一次cmm接口获取全部用户资料，初始化用户名和电话。
    user_info_list = batch_get_user_info(user_id_list)
    user_info_list_new = []
    for item in user_info_list:
        data = {}
        if 'nickname' in item:
            data['user_name'] = item['nickname']
        else:
            data['user_name'] = 'system'
        if 'phone' in item:
            data['user_phone'] = item['phone']
        else:
            data['user_phone'] = '18988888888'
        if len(data) > 0:
            data['user_id'] = item['id']
            user_info_list_new.append(data)
    return user_info_list_new


if __name__ == '__main__':
    li = batch_get_user_info_list([10000024, 10000118])
    print(li)
