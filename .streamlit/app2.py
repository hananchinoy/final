import streamlit as st
st.title("*The Conscious Choice.*")
magicEnabled = False
st.markdown ("In solidarity with :flag-ps:, this app is designed to help you make conscious choices and avoid purchasing products or services from companies that support and/or fund the gen0cide in Gaza.")
st.markdown (":green[Type in the product's name or the parent company name to find out whether the brand or company is among those on the boycott list.]")



name= (st.text_input("Enter Brand Name (full name is preferred)"))

def checkValue(value,boycottList): 
 if name != "":

   if(value.casefold() in (name.casefold() for name in boycottList)):
    st.markdown(":red[_This brand is boycotted!_]");
     
   else: 
     st.markdown(":green[_This brand is not on the boycott list, you may purchase their products._]");
   

boycott = ['Lidl', 'Coca cola', 'McDonalds', 'Mcd', 'Mcdonalds' ,'Mcdonald',"Starbucks" ,'Puma', 'Wix', 'wix.com', 'AXA', 'Siemens', 'Nestle', 'Airbnb', 'Volvo', 'Caterpillar', 'Motorola', 'Pampers', 'LOreal', 'Loreal', 'Lancôme',
'Yves Saint Laurent', 'Giorgio Armani', 'giorgo armani', 
'Kiehls', 'Urban Decay', 'Biotherm', 'Maybelline', 'Garnier', 'Marks & Spencer', 'Smartwater', 'lipton', 'hardees','kfc', 'KFC', 'hasbro',
'NYX','Kerastase','Redken', 'Hasbro', 'Mattel', 'lego', 'clorox', 'lululemon', 'unilever', "hershey's", 'costa coffee', 'American Eagle', 'The Body Shop', 'Tommy Hilfiger', 'Johnson and Johnson', 'Covergirl', 'Nesquik', 'Papa Johns','Tropicana', 'Pizza Hut', 'Dominos', 'Kit Kat', 'Burger King', 'Häagen-Dazs', "ford", "levi's" 'La Roche Posay','Vichy','SkinCeuticals', 'skin ceuticals','CeraVe', 'cerave', 'nyx', 'rhode skin', 'rhode','fenty beauty', 'fenty', 'dior', 'clinique','chanel', 'bvlgari','bobbi brown', 'bath and body works', 'bath & body works', 'aesop', 'estee lauder', 'head & shoulders', 'head and shoulders', 'herbal essences', 'kylie cosmetics', 'skims', 'louis vuitton', 'MAC', 'moroccan oil', 'pantene', 'the ordinary', 'victorias secret', 'YSL', 'Yves Saint Laurent', 'walmart', 'rare beauty', 'Adidas',
'Reebok', 'bath and body', 'michael kors', 'the body shop', 'cocacola',
'Under Armour', "mcdonald's", 'pampers',
'New Balance', 'H&M', 'h and m', 'H & M',
'ASICS','Vans','Converse','Skechers',
'Dell', 'hp', 'intel', 'nvidia', 'carrefour', 'fanta', 'sprite', 'lays', 'marks and spencer', 'minute maid', 'pepsi', 'pepsico', 'pepsiCo', 'pepsi co', 'sabra', 'sodastream', 'soda stream', 'strauss', 'zara', 'Pull&Bear', 'pull and bear', 'amazon', 'booking.com', 'expedia', 'expedia group', 'fiverr', 'monday.com', 'trip advisor', 'tripAdvisor', 'wix', 'Bersheka', 'Stradivarious', 'disney', 'netflix', 'toyota', 'unilever', 'volkswagen', 'Axe', 'lancome','Ben & Jerry', 'ben and jerry','Cif',
'Comfort', 'always','foster clarks', "Maggi", 'pringles', 'oreo', 'fanta', 'sprite', 'coca cola', 'milo', 'subway', 'maggie', 'kit kat', 'lifebuoy', 'huggies', 'gillette', 'walmart', 'nescafe', 'doritos', 'amazon.com', 'amazon', 'oral B', 'colgate', 'netafim', 'oracle', 'pepsodent', 'nokia', 'cheetos', 'motorola', 'forbes', 'pantene', 'sunsilk', 'dove', 'nvidia', 'carrefour', 'gucci', "victoria's secret", "l'oreal", 'nivea', 'olay', 'aquafina', 'lux', 'dalda', 'Bershka', 'Massimo Dutti', 'Oysho', 'Stradivarius', 'Uterqüe', 'cadbury', 'dairy milk', 'twix', 'mars', 'snickers', 'bounty', 'milky way',
"foster clark's", 'Dove',
'Hellmann', 'lefties',
'Knorr',
'LUX', 'galaxy', 
'Magnum',
'OLLY Vitamins',
'OMO', 'ariel',
'Rexona',
'SmartyPants Vitamins',
'Sunsilk',
'Vaseline',
'Walls','dettol', 'sephora', 'prada']  
checkValue(name,boycott)
st.markdown (":grey[Please note that this app recognizes the boycotted companies in the _Cosmetics, F&B, Entertainment, Apparel and Technology_ sectors]")
st.image('https://img.freepik.com/free-vector/illustrated-peace-message-background_23-2148969870.jpg?w=740')
st.markdown (":grey[Image Credits: Freepik]")
st.markdown (":grey[© Hanan Chinoy. All rights reserved.]")
