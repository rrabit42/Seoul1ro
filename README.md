# Seoul1ro
## Junction X Seoul 2021  
### SI Analysis track  

## Idea  
### ๐Fire station Loacation Analysis๐ฅ  
Provide a recommendation on fire station location in areas where skyscrapers and houses are concentrated.
The importance of providing rapid fire service is highlighted because citizens' safety is exposed due to disasters.
Service analysis is needed for efficient fire station location to resolve disaster safety blind spots and provide equal fire service.  

### ๐กProposal Algorithm  
* **Scale for fire station**  
Determine if the space is large enough for a fire station.  
* **Adjacent to dense residential areas**  
In areas where houses are concentrated, providing rapid fire swervice becomes more important.  
* **The ratio of the area of the road to the building**  
Calculate the ratio of the area of the road to the building to determine if the passage is guaranteed.  

<img width="749" alt="1" src="https://user-images.githubusercontent.com/46364778/119251667-b34b6d80-bbe2-11eb-823a-35769adc8e8d.PNG">  

<img width="746" alt="2" src="https://user-images.githubusercontent.com/46364778/119251668-b47c9a80-bbe2-11eb-9302-ac91c2be45f9.PNG">  


## Demo  
![bandicam 2021-05-23 15-34-55-400](https://user-images.githubusercontent.com/46364778/119250693-d410c480-bbdc-11eb-898b-ef582fecd671.gif)  

## Seoul1ro Team members
* ๐ฒ**Yurhee Jin**: Entrepreneur & AI development
* ๐ฒ**Jihye Shin**: Entrepreneur
* ๐ฒ**Yeonsoo Choi**: Designer
* ๐ฒ**Jisoo Kim**: AI development
* ๐ฒ**Sunwoo Ho**: Frontend development
* ๐ฒ**SeoYoung Kim**: Backend development

## Django ์คํ
1. pycharm interpreter์์ ๊ฐ์ํ๊ฒฝ ํด๋ ์ค์   
2. ```pip install -r requirements.txt```  
3. ```python manage.py makemigrations```  
4. ```python manage.py migrate```  
5. ```python manage.py runserver```  
```python manage.py collectstatic``` : static ํ์ผ ์ถ๊ฐํ์ ๋  

## Conda ๋์ ์คํ  
1. ```conda env create -f environment.yml``` : yml ๊ฒฝ๋ก๋ ์์์ ์์   
2. ```conda activate label-pixels```
