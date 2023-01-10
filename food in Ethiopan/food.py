import streamlit as st
from PIL import Image


st.title("Famous Foods Eaten in Ethiopa")

st.write("""
	Ethiopian cuisine is a rich and diverse blend of various cultural influences, 
	including indigenous, Mediterranean, and Indian. 
	Some of the most famous and delicious foods enjoyed in Ethiopia include:
""")
Injera_col1,Injera_col2=st.columns(2)

with Injera_col1:	
	st.subheader("1. Injera")
	st.write("""
	This is a sourdough flatbread that is a staple in Ethiopian cuisine. 
	It is made from teff flour, which is a type of grain that is unique to Ethiopia. 
	Injera is often served as the base for other dishes, such as stews and vegetables, 
	and is used to scoop up the food and bring it to the mouth.
	Injera is made by mixing teff flour with water, and then allowing the mixture to ferment for a few days. 
	This fermentation process gives injera its characteristic sour taste and spongy texture. 
	Once the mixture is ready, it is cooked on a large, flat griddle, similar to a crepe. 
	
	""")
with Injera_col2:
	Injera=Image.open('Injera.png')
	st.image(Injera,caption="Injera")



st.write("""
	The finished injera is usually about half a centimeter thick and can be up to a meter in diameter.
	Injera is typically served with various stews, called "wat" or "tsebhi", that are made with meat or vegetables. 
	The stews are typically served on top of the injera, which is then rolled up or torn into pieces to be used as a utensil to scoop up the stew. 
	It's also common to use injera as a wrap for different types of meats,spicy or mild sauces,fruits, and vegetables.
	There are different variations of injera in Ethiopia and Eritrea, depending on the region. 
	Some people make injera with a combination of teff flour and other types of flour, such

""")


st.write("\n\n\n\n\n\n\n\n\n")


Doro_Wat_col1,Doro_Wat_col2=st.columns(2)

with Doro_Wat_col1:
	st.subheader("2. Doro Wat")
	st.write("""
		This is a spicy chicken stew that is a popular dish in Ethiopia. 
		It is made with red pepper, ginger, garlic, and other spices, as well as onions, tomato, and often served with injera.
		To make Doro Wat, the chicken is first marinated in a mixture of spices, including ginger, garlic, and berbere. 
	
	"""
	)

with Doro_Wat_col2:
	DoroWat=Image.open('DoroWat.png')
	st.image(DoroWat,caption="Doro Wat")


st.write("""
	The marinated chicken is then sautéed with onions, and simmered in a flavorful sauce made from a combination of berbere, butter, and a traditional Ethiopian spice blend called mitmita.  
	The sauce is thickened with flour or sometimes with ground nuts like peanut.
	Doro Wat is considered as a celebratory dish and it is common in traditional festivals, holidays, and important events such as weddings, and it also served as a comfort food.
	If you want to try making Doro Wat at home, you can find many variations of the recipe online, each with its own unique combination of spices and ingredients.  A lot of it depends on the specific ingredient availability and traditions of the region as well.
""")

st.write("\n\n\n\n\n\n\n\n\n")

Tibs_col1,Tibs_col2=st.columns(2)

with Tibs_col1:
	st.subheader("3. Tibs")
	st.write("""
		These are sautéed or grilled meat dishes that are a common sight at Ethiopian restaurants. 
		They can be made with a variety of meats, including beef, lamb, chicken, and fish, 
		and are typically seasoned with a combination of spices such as berbere, a spice blend that is a staple of Ethiopian cooking.
		
	"""
	)

with Tibs_col2:
	Tibs=Image.open("Tibs.png")
	st.image(Tibs,caption="Tibs")

st.write("""
	Tibs is a type of Ethiopian dish made with meat, vegetables, and spices. 
	The meat is typically cut into small pieces and sautéed with onions, tomatoes, and other vegetables. 
	Spices such as berbere, a blend of chili peppers and other spices, are commonly used to add flavor. 
	Tibs can be made with a variety of meats, including beef, lamb, chicken, or even fish. 
	It's often served with injera, a traditional Ethiopian flatbread made from teff flour, which is used to scoop up the meat and vegetables.
"""
)


Kitfo_col1,Kitfo_col2=st.columns(2)

with Kitfo_col1:
	st.subheader("4. Kitfo")
	st.write("""
		This is a traditional Ethiopian dish made of raw minced meat, usually beef, that is often served with bread or injera. 
		It is similar to steak tartare and it's usually served with a side of spices, 
		including chili powder and mitmita, a hot spice blend made from chili peppers, ginger, and other spices.
	"""
	)


with Kitfo_col2:
	Kitfo=Image.open('Kitfo.png')
	st.image(Kitfo,caption="Kitfo")
	
st.write("""
	The meat is usually minced finely and mixed with spices and sometimes with butter called niter kibbeh. 
	The dish is generally considered a delicacy, and it is often served at special occasions and celebrations. 
	Kitfo is often served raw, but it can also be served cooked, which is called leb leb kitfo.
	It's also a must try for a foodie people who love trying different kinds of food.Please note that consuming raw or undercooked meat, 
	especially beef poses risk of foodborne illnesses. If you choose to try kitfo, it's best to make sure it's prepared properly and with good hygiene.
"""
)

Shiro_col1,Shiro_col2=st.columns(2)
with Shiro_col1:
	st.subheader("5. Shiro")
	st.write("""
		This is a thick stew that is made from ground chickpeas, lentils, or split peas. 
		It is a popular vegan dish and is often served with injera or bread.
		Ethiopian food shiro is a hearty and healthy dish that is high in protein and fiber, low in fat, and nutrient-rich. 
		It is made from chickpea flour and simply seasoned with garlic, onions, and spices like berbere. 
		
	""")
with Shiro_col2:
	Shiro=Image.open('Shiro.png')
	st.image(Shiro,caption="Shiro")
	
st.write("""
	It is a great source of energy and can help regulate blood sugar levels. 
	And is also an excellent source of vitamins and minerals and may help reduce inflammation and boost the immune system.
	It can also be used as a side dish or as a main dish when it is served with injera or other breads.
	The range of Ethiopian food is also represented by the vegetarian and vegan dishes. 
	Many of the traditional dishes can easily be veganized, thanks to the generous use of beans and lentils in the cuisine. 
	For example, misir wat is a dish made from red lentils that is served with a variety of spices. 
	Gomen is another vegan-friendly dish, which consists of collard greens cooked with onion, garlic, and oil.
	
	No matter what a diner's tastes may be, there is most likely an Ethiopian dish to suit them. 
	From spiced lentils to spicy chicken dishes, Ethiopian food is full of flavorful combinations that have been perfected over centuries. 
	Whether served in a traditional Ethiopian restaurant or served as part of a fusion menu, 
	Ethiopian food is both delicious and culturally enriching.
	
	
""")


st.subheader("Conclusion")
st.write("""
	Ethiopian food is a unique and flavorful style of cuisine that has been perfected over centuries. 
	From traditional dishes such as injera and shiro to the more modern dishes like teff breads and stews, 
	Ethiopian food is full of flavor, texture, and vibrant aromas. 
	Thanks to its vegetarian-friendly dishes, its vegan-friendly dishes, and its range of condiments and spices, 
	Ethiopian food is sure to satisfy all types of taste buds. 
	It is a true taste of heaven that must be experienced!
"""
)
