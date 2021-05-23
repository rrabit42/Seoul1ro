# Seoul1ro
## Junction X Seoul 2021  
### SI Anaylisis track  

## Idea  
### 🚒Fire station Loacation Analysis🔥  
Provide a recommendation on fire station location in areas where skyscrapers and houses are concentrated.
The importance of providing rapid fire service is highlighted because citizens' safety is exposed due to disasters.
Service analysis is needed for efficient fire station location to resolve disaster safety blind spots and provide equal fire service.  

### 💡Proposal Algorithm  
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
* 🌲**Yurhee Jin**: Entrepreneur & AI development
* 🌲**Jihye Shin**: Entrepreneur
* 🌲**Yeonsoo Choi**: Designer
* 🌲**Jisoo Kim**: AI development
* 🌲**Sunwoo Ho**: Frontend development
* 🌲**SeoYoung Kim**: Backend development

## Django 실행
1. pycharm interpreter에서 가상환경 폴더 설정  
2. ```pip install -r requirements.txt```  
3. ```python manage.py makemigrations```  
4. ```python manage.py migrate```  
5. ```python manage.py runserver```  
```python manage.py collectstatic``` : static 파일 추가했을 때  

## Conda 동시 실행  
1. ```conda env create -f environment.yml``` : yml 경로는 알아서 수정  
2. ```conda activate label-pixels```
