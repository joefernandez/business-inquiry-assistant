# training examples

import json

prompt_1 = dict(prompt = """
Hi Indian Bakery Central,
Do you happen to have 10 pendas, and thirty bundi ladoos on hand? Also do you sell a vanilla frosting and chocolate flavor cakes. I'm looking for a 6 inch size
""",
response = json.loads("""
  {
    "type": "inquiry",
    "items": [
      {
        "name": "pendas",
        "quantity": 10
      },
      {
        "name": "bundi ladoos",
        "quantity": 30
      },
      {
        "name": "cake",
        "filling": null,
        "frosting": "vanilla",
        "flavor": "chocolate",
        "size": "6 in"
      }
    ]
}
""")
)

prompt_2 = dict(prompt = """
I saw your business on google maps. Do you sell jellabi and gulab jamun?
""",
response = json.loads("""
  {
    "type": "inquiry",
    "items": [
      {
        "name": "jellabi",
        "quantity": null
      },
      {
        "name": "gulab jamun",
        "quantity": null
      }
    ]
}
""")
)

prompt_3 = dict(prompt = """
I'd like to place an order for a 8 inch red velvet cake with lemon frosting and chocolate chips topping.
""",
response = json.loads("""
  {
    "type": "order",
    "items": [
      {
        "name": "cake",
        "filling": "8inch",
        "frosting": "lemon",
        "flavor": "chocolate",
        "size": "8 in"
      }
    ]
}
""")
)

prompt_4 = dict(prompt = """
I'd like four jellabi and three gulab Jamun.
""",
response = json.loads("""
  {
    "type": "order",
    "items": [
      {
        "name": "Jellabi",
        "quantity": 4
      },
      {
        "name": "Gulab Jamun",
        "quantity": 3
      }
    ]
}
""")
)

prompt_4_2 = dict(prompt = """
Please pack me a box with 10 halva.
""",
response = json.loads("""
  {
    "type": "order",
    "items": [
      {
        "name": "halva",
        "quantity": 10
      }
    ]
}
""")
)

prompt_5 = dict(prompt = """
Do you sell strawberry cakes with vanilla frosting with custard inside?
""",
response = json.loads("""
  {
    "type": "inquiry",
    "items": [
      {
        "name": "cake",
        "filling": "custard",
        "frosting": "vanilla",
        "flavor": "strawberry",
        "size": "null"
      }
    ]
}
""")
)

prompt_5_2 = dict(prompt = """
Do you sell carrot cakes with cream cheese frosting?
""",
response = json.loads("""
  {
    "type": "inquiry",
    "items": [
      {
        "name": "cake",
        "filling": "null",
        "frosting": "cream cheese",
        "flavor": "carrot",
        "size": "null"
      }
    ]
}
""")
)

prompt_6 = dict(prompt = """
I found your website. What kind of items do you sell?
""",
response = json.loads("""
  {
    "type": "inquiry",
    "items": [
    ]
}
""")
)

# Starts overfitting on lemon if you add this

# prompt_7 = dict(prompt = """
# Can I buy 18 halva, as well as a lemon cake with lemon frosting?
# """,
# response = json.loads("""
#   {
#     "type": "inquiry",
#     "items": [
#       {
#         "name": "halva",
#         "quantity": 18
#       },
#       {
#         "filling": null,
#         "frosting": "lemon",
#         "flavor": "lemon",
#         "size": null
#       }
#     ]
# }
# """)
# )