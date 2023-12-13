import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()

from django_seed import Seed
from restaurants.models import Restaurant
from users.models import User
from reviews.models import Review 
import random

korean_sentences = [
    "음식들이 다 정말 맛있어요! 재방문 의사 있어요!. 음식이 부드럽고 식감이 좋아 두고 두고 기억에 남는 맛이었습니다",
    "서비스도 친절하고 분위기도 아주 좋아서 자주 방문하게 되네요. 정말 고급스러워서 다음에 또 방문하고 싶어지는 곳이에요" ,
    "양도 푸짐해서 배부르게 식사할 수 있습니다. 여러 차례 다른 집들을 찾았지만 결국 여기로 돌아오게 되네요",
    "각 음식마다 정성이 느껴져서 특별한 날이나 손님 맞이할 때 딱인 곳입니다",
    "양념소스가 정말 고급스러워서 다음에 또 방문하고 싶어지는 곳이에요",
    "여러 재료들이 신선하게 들어가 있어서 건강한 식사를 할 수 있었어요",
    "사장님의 정성스러운 서비스가 인상적이에요, 각 음식마다 정성이 느껴져서 특별한 날이나 손님 맞이할 때 딱인 곳입니다",
    "여러 차례 다른 집들을 찾았지만 결국 여기로 돌아오게 되네요",
    "음식이 부드럽고 식감이 좋아 두고 두고 기억에 남는 맛이었습니다",
    "맥주 한 잔하면서 가볍게 즐길 수 있는 곳이에요, 음식이 부드럽고 식감이 좋아 두고 두고 기억에 남는 맛이었습니다",
    "각 음식의 정성이 느껴져서 정말 가족이나 친구와 함께 음식들을 한 자리에서 즐길 수 있었습니다",
    "국물이 깊고 감칠맛이 일품이에요, 각 음식마다 정성이 느껴져서 특별한 날이나 손님 맞이할 때 딱인 곳입니다",
]

korean_menu = [
    "김치찌개",
    "된장찌개",
    "찜닭",
    "불고기",
    "비빔밥",
    "김밥",
    "만두",
    "떡볶이",
    "순대국밥",
    "뼈해장국",
    "감자탕",
    "족발",
    "보쌈",
    "해물찜",
    "쌈밥",
    "냉면",
    "육회",
    "간장게장",
    "해물파전",
    "쭈꾸미볶음",
    "장어구이",
    "곱창",
    "막창",
    "초밥",
    "라면",
    "우동",
    "탕수육",
    "짬뽕",
    "팟타이",
    "쌀국수",
    "쌈장국수",
    "훠궈",
    "샤브샤브",
    "치킨",
    "피자",
    "햄버거",
    "스테이크",
    "샐러드",
    "파스타",
    "리조또",
    "스시",
    "회",
    "죽",
    "보리밥",
    "쌀밥",
    "볶음밥",
    "김치볶음밥",
    "오므라이스",
    "김치전",
    "파전",
    "계란찜",
    "갈비탕",
    "삼계탕",
    "추어탕",
    "미역국",
    "된장국",
    "북엇국",
    "어묵국",
    "호박죽",
    "닭곰탕",
    "야채튀김",
    "고추튀김",
    "오징어튀김",
    "계란후라이",
    "간장게장",
    "마파두부",
    "짜장면",
    "짬뽕",
    "볶음밥",
    "양장피",
    "볶음우동",
    "쟁반짜장",
    "짬짜면",
    "팔보채",
    "사천짜장",
    "탕수육",
    "군만두",
    "치즈라면",
    "김치볶음우동",
    "깐풍기",
    "양념치킨",
    "간장치킨",
    "후라이드치킨",
    "양념후라이드",
    "갈비치킨",
    "마늘치킨",
    "레드커리",
    "로제파스타",
    "알리오올리오",
    "크림파스타",
    "해물파스타",
    "까르보나라",
    "바베큐스테이크",
]

seeder = Seed.seeder()
restaurant_ids = list(range(1, 4511))  
user_id = 1

for restaurant_id in restaurant_ids:        
    seeder.add_entity(Review, 3, {
        'restaurant': Restaurant.objects.get(pk=restaurant_id),
        'user': User.objects.get(pk=user_id),
        'stars': lambda x: seeder.faker.random_int(min=1, max=5),
        'contents': lambda x: random.choice(korean_sentences),
        'menu': lambda x: [random.choice(korean_menu) for _ in range(seeder.faker.random_int(min=1, max=5))],
        'images': [],
    })

inserted_pks = seeder.execute()

print(f"Dummy data inserted. Review IDs: {inserted_pks[Review]}")
