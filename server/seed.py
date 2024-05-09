from random import randint, choice as rc
from app import app
from models import db, Tshirt, Hoodie, Shastar

# Remote library imports
with app.app_context():
    db.drop_all()
    db.create_all()
    
    tshirts = [
        Tshirt(
            name='Misl O',
            description='Classic Corduroy Shirt - Breathable Short-Sleeve Button-Up with Sharp Lapel Collar - Casual Summer Wear',
            price='25.99',
            image_url='https://i.ibb.co/FxKcn3X/TS1.jpg'
            
            
        ),
        Tshirt(
            name='Misl Br',
            description='Classic Corduroy Shirt - Breathable Short-Sleeve Button-Up with Sharp Lapel Collar - Casual Summer Wear',
            price='25.99',
            image_url='https://i.ibb.co/cx4qwLR/TS2.jpg'
        ),
        Tshirt(
            name='Misl Sea',
            description='Classic Corduroy Shirt - Breathable Short-Sleeve Button-Up with Sharp Lapel Collar - Casual Summer Wear',
            price='25.99',
            image_url='https://i.ibb.co/GQH6Kkz/TS3.jpg'
        ),
        Tshirt(
            name='World G',
            description='Cartoon Polyester Astronaut And Planet Print Tee Best Sellers',
            price='19.99',
            image_url='https://i.ibb.co/60snnWM/TS4.jpg'
        ),
        Tshirt(
            name='World B',
            description='Cartoon Polyester Astronaut And Planet Print Tee Best Sellers',
            price='19.99',
            image_url='https://i.ibb.co/ZY0VBZk/TS5.jpg'
        ),
        Tshirt(
            name='Misl B',
            description='Cotton Soft Crew Neck Short Sleeve Lounge Basic T-shirt Plain Color',
            price='17.99',
            image_url='https://i.ibb.co/F0vGcvw/TS6.jpg'
        ),
        Tshirt(
            name='Misl G',
            description='Cotton Soft Crew Neck Short Sleeve Lounge Basic T-shirt Plain Color',
            price='17.99',
            image_url='https://i.ibb.co/4F7cn1M/TS7.jpg'
        )
    ]
    db.session.add_all(tshirts)
    
    hoodies = [
        Hoodie(
            name='Retro1',
            description='Retro Color Block Streetwear, Cool Hoodies For Men, Mens Casual Graphic Design Pullover Hooded Sweatshirt For Winter Fall, As Gifts',
            price='19.99',
            image_url='https://i.ibb.co/tDB4XKX/hoodie1.jpg'
        ),
        Hoodie(
            name='Retro2',
            description='Retro Color Block Streetwear, Cool Hoodies For Men, Mens Casual Graphic Design Pullover Hooded Sweatshirt For Winter Fall, As Gifts',
            price='19.99',
            image_url='https://i.ibb.co/K0dT7WR/hoodie2.jpg'
        ),
        Hoodie(
            name='E Trendy B',
            description='Trendy Solid Mens Hooded Sweatshirt With Kangaroo Pocket, Mens Pullover Tops For Fall Winter',
            price='15.99',
            image_url='https://i.ibb.co/XZPbrpW/hoodie3.jpg'
        ),
        Hoodie(
            name='Ulimate ET',
            description='Houndstooth Pullover Round Neck Hoodies With Kangaroo Pocket Trendy Fashion Long Sleeve Hooded Sweatshirt, Loose Casual Top For Autumn Winter, Mens Clothing As Holiday Gift',
            price='39.99',
            image_url='https://i.ibb.co/CKCk3XP/hoodie4.jpg'
        ),
        Hoodie(
            name='E Trendy W',
            description='Trendy Solid Mens Hooded Sweatshirt With Kangaroo Pocket, Mens Pullover Tops For Fall Winter',
            price='15.99',
            image_url='https://i.ibb.co/5vWyncH/hoodie5.jpg'
        ),
        Hoodie(
            name='E Trendy R',
            description='Trendy Solid Mens Hooded Sweatshirt With Kangaroo Pocket, Mens Pullover Tops For Fall Winter',
            price='15.99',
            image_url='https://i.ibb.co/hXtpq8d/hoodie6.jpg'
        )
    ]
    db.session.add_all(hoodies)
    
    shastars = [
        Shastar(
            name='Moranwali',
            description='Hand Made Kirpan, Moranwali Kirpan made of Sarbhloh, Leather Case',
            price='99.99',
            image_url='https://i.ibb.co/G5cJtRj/C7035463-F451-4368-A77-D-1-F4-DB54-EA75-A.jpg'
        ),
        Shastar(
            name='Katar',
            description='Sikh Shastar, Sarbhloh Sikh blade, Khanjar, kamani katar, handforged blade, sharp blade, pattern design on blade',
            price='99.99',
            image_url='https://i.ibb.co/J7LqHLp/74-C0-C484-07-A7-4-C68-AFC5-46-F38025-BCBD.jpg'
        ),
        Shastar(
            name='Zulfikar',
            description='Zulfikar, Big Kirpan, 3 foot kirpan, Shastar',
            price='199.99',
            image_url='https://i.ibb.co/2dtqb8y/FBC5-A4-C2-2-C07-4-A3-B-9-CDC-EA8-B22896042.jpg'
        ),
        Shastar(
            name='Khanda',
            description='Big Khanda, Kirpan, Sarbhloh Khanda, Sikh kakar, 3 foot,',
            price='199.99',
            image_url='https://i.ibb.co/c3WmhFV/9-F25-D9-D7-5-B95-440-C-8-B74-BCDDB132-A0-DE.jpg'
        ),
        Shastar(
            name='Kakkar',
            description='Kirpan, Sikh kakar, Sikh Sword, Sikh Kakkar, Sikh Shastar',
            price='159.99',
            image_url='https://i.ibb.co/82FysmX/FCE3-D5-FA-34-AC-4-C9-E-91-E1-EC9-E0-C7-C6-E11.jpg'
        ),
        Shastar(
            name='Clean Cut',
            description='Wedding Kirpan, Brass Sword, Punjabi Viah, Punjabi Wedding accessory, Sikh Wedding items',
            price='399.99',
            image_url='https://i.ibb.co/YT6PHhF/F47-F97-A8-C55-C-47-FF-925-E-4-A04-A984-BEA9.jpg'
            
        )
        
    ]
    db.session.add_all(shastars)
    
    db.session.commit()
    print('Database seeded!')
