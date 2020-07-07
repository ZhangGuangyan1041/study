def build_profile(first, last, **user_info):
    """创建一个用户，其中包含我们知道的一切信息"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile("albert", "einstein", location="princeton", field="physics")
print(user_profile)
