# 创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['iphone case','robot pendant', 'dodecahedron']
completed_models = []

# 模拟打印每个设计，知道没有未打印的设计为止
# 打印每个设计后，将其放入列表completed_models
while unprinted_designs:
    current_design = unprinted_designs.pop()

    # 模拟根据设计制作3D打印模型的过程
    print("Printing model :" + current_design)
    completed_models.append(current_design)
# 显示打印所有的模型
for completed_model in completed_models:
    print("model is " + completed_model)


def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    for completed_model in completed_models:
        print(completed_model)


print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
