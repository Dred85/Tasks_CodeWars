
def cakes(recipe, ingredients):
    # Список количества тортов для хранения отношений количества каждого ингредиента в рецепте к доступному количеству
    ratios = []

    # Проходимся по каждому ингредиенту в рецепте
    for ingredient, amount in recipe.items():
        # Если в доступных ингредиентах нет текущего ингредиента из рецепта,
        # то возвращаем 0, потому что мы не можем приготовить ни одного пирога
        if ingredient not in ingredients:
            return 0
        # Вычисляем отношение количества ингредиента из рецепта к доступному количеству
        ratio = ingredients[ingredient] // amount
        # Добавляем отношение в список
        ratios.append(ratio)

    # Возвращаем минимальное значение из списка отношений
    return min(ratios)


recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
print(cakes(recipe, available))
