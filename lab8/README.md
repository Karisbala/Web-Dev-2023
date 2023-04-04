# Online Shop

In this laboratory work you have to start preparing an API for your app from *Lab 5*.

Create a django project with the name “*shop-back*”.
1. Project contains application with name - *api*  
2. You have model with following fields:
    - *Product*
        1. name - CharField
        2. price - FloatField
        3. description - TextField
        4. count - IntegerField
        5. is_active - BooleanField
    - *Category*
        1. name - CharField
3. Write API endpoints with JSON format:
    - */api/products* - List of all Products
    - */api/products/<int:id>/* - Get one Product
    - */api/categories/* - List of all Categories
    - */api/categories/<int:id>/* - Get one Category
    - */api/categories/<int:id>/products/* - List of Products by Category




GOOD LUCK :)
