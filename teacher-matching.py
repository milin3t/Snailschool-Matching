import random

# 남교사 명단
# (,,) <- 이름, 신입, 지인
male_teachers = [
    ("###", False, False),
    ("###", True, False),
    ("###", True, False),
    ("###", True, True),
    ("###", True, True),
    ("###", True, True),
    ("###", True, False)
]

# 여교사 명단
# (,,) <- 이름, 신입, 지인
female_teachers = [
    ("###", False, False),
    ("###", False, False),
    ("###", False, True),
    ("###", True, False),
    ("###", True, False),
    ("###", True, False),
    ("###", True, True)
]


# 가능한 매칭 후보 생성
def is_valid_match(male, female, allow_new_to_new=False):
    if male[1] == female[1]:
        return allow_new_to_new and male[1]    # 신입-신입만 예외적으로 허용
    if male[2] and female[2]:  
        return False                           # 지인끼리 매칭 금지
    return True


# 1차 : 기본 규칙 적용
valid_pairs = [(m, f) for m in male_teachers for f in female_teachers if is_valid_match(m, f)]
random.shuffle(valid_pairs)

matching = []
used_males = set()
used_females = set()

for male, female in valid_pairs:
    if male[0] not in used_males and female[0] not in used_females:
        matching.append((male[0], female[0]))
        used_males.add(male[0])
        used_females.add(female[0])


# 2차 : 부족한 경우 신입-신입만 허용, 지인끼리 매칭 안 되도록
if len(matching) < 7:
    remaining_males = [m for m in male_teachers if m[0] not in used_males]
    remaining_females = [f for f in female_teachers if f[0] not in used_females]
    
    extra_pairs = [
        (m, f) for m in remaining_males for f in remaining_females
        if is_valid_match(m, f, allow_new_to_new=True) and not (m[2] and f[2])
    ]
    
    random.shuffle(extra_pairs)
    
    for male, female in extra_pairs:
        if len(matching) >= 7:
            break
        if male[0] not in used_males and female[0] not in used_females:
            matching.append((male[0], female[0]))
            used_males.add(male[0])
            used_females.add(female[0])


# 3차 : remainder에 대해 무조건적인 매칭
if len(matching) < 7:
    remaining_males = [m for m in male_teachers if m[0] not in used_males]
    remaining_females = [f for f in female_teachers if f[0] not in used_females]
    
    for male in remaining_males:
        for female in remaining_females:
            if len(matching) >= 7:
                break
            if male[0] not in used_males and female[0] not in used_females:
                matching.append((male[0], female[0]))
                used_males.add(male[0])
                used_females.add(female[0])


# Result
for male, female in matching:
    print(f"{male} - {female}")
