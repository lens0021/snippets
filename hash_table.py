from enum import Enum
import random


class CollisionResolutionStrategy(Enum):
    LINEAR_PROBING = 0
    QUADRATIC_PROBING = 1
    CHAINING = 2


DEBUG = True  # 참이면 디버그 로그를 출력합니다.
SCENARIO_NUMBER = 0  # 사용할 시나리오를 고릅니다.
USE_RANDOM_SEED = False  # 참이라면 시드를 사용합니다.
COLLISION_RESOLUTION_STRATEGY = CollisionResolutionStrategy.LINEAR_PROBING

# 해시 테이블의 크기는 소수가 되어야 하는데, 계산하기 번거로우므로 미리 몇 개 적어 놓음.
prime_numbers = [2, 3, 4, 7, 11, 13, 17,
                 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]

TOMBSTONE = 'tombstone'


# 해시 테이블 초기화
hash_table = [None for _ in range(prime_numbers[6])]

# Pearsen hash에 필요한 Lookup Table 초기화
lookup_table = list(range(256))
if USE_RANDOM_SEED:
    random.Random(0).shuffle(lookup_table)
else:
    random.shuffle(lookup_table)


def pearson_hash_function(key: str) -> int:
    hash = 0
    for ch in key:
        hash = lookup_table[hash ^ (ord(ch) % 256)]

    return hash % len(hash_table)


def hash_table_add(key: str, val: str):
    if COLLISION_RESOLUTION_STRATEGY == CollisionResolutionStrategy.LINEAR_PROBING:
        starting_index = idx = pearson_hash_function(key)

        while hash_table[idx] != None:
            if hash_table[idx] != TOMBSTONE and hash_table[idx][0] == key:
                if DEBUG:
                    print('탐색 키가 중복되었습니다.')
                return
            idx = (idx + 1) % len(hash_table)
            if idx == starting_index:
                if DEBUG:
                    print('해시테이블이 가득 찼습니다.')
                # TODO 테이블 늘려서 추가하기
                return
        print(f'{idx}에 {key} 추가')
        hash_table[idx] = (key, val)
    elif COLLISION_RESOLUTION_STRATEGY == CollisionResolutionStrategy.QUADRATIC_PROBING:
        pass  # TODO
    elif COLLISION_RESOLUTION_STRATEGY == CollisionResolutionStrategy.CHAINING:
        idx = pearson_hash_function(key)

        hash_table[idx].append((key, val))


def hash_table_search(key: str):
    if COLLISION_RESOLUTION_STRATEGY == CollisionResolutionStrategy.LINEAR_PROBING:
        starting_index = idx = pearson_hash_function(key)
        while hash_table[idx] != None:
            if hash_table[idx] != TOMBSTONE:
                stored_key, val = hash_table[idx]
                if stored_key == key:
                    return val
            else:
                pass

            if DEBUG:
                print(f'{key}를 불러오는 도중 충돌 발견')

            idx = (idx+1) % len(hash_table)
            if idx == starting_index:
                if DEBUG:
                    print(f'값이 없음')
                return None
            else:
                pass

        print(f'값이 없음')
        return None
    elif COLLISION_RESOLUTION_STRATEGY == CollisionResolutionStrategy.QUADRATIC_PROBING:
        pass  # TODO
    elif COLLISION_RESOLUTION_STRATEGY == CollisionResolutionStrategy.CHAINING:
        idx = pearson_hash_function(key)

        return val


def hash_table_delete(key: str):
    if COLLISION_RESOLUTION_STRATEGY == CollisionResolutionStrategy.LINEAR_PROBING:
        starting_index = idx = pearson_hash_function(key)
        while hash_table[idx] != None:
            if hash_table[idx] != TOMBSTONE:
                if hash_table[idx][0] == key:
                    if DEBUG:
                        print(f'{idx}에 있던 {key} 삭제')
                    hash_table[idx] = TOMBSTONE
                    return
            else:
                pass

            if DEBUG:
                print(f'{key}를 삭제하는 도중 충돌 발견')

            idx = (idx+1) % len(hash_table)
            if idx == starting_index:
                if DEBUG:
                    print(f'값이 없음')
                return
            else:
                pass

        print(f'값이 없음')
        return None
    elif COLLISION_RESOLUTION_STRATEGY == CollisionResolutionStrategy.QUADRATIC_PROBING:
        pass  # TODO
    elif COLLISION_RESOLUTION_STRATEGY == CollisionResolutionStrategy.CHAINING:
        pass  # TODO


def hash_table_update(key: str, val: str):
    # TODO 호출 대신 직접 짜기
    hash_table_delete(key)
    hash_table_add(key, val)


if SCENARIO_NUMBER == 0:
    # 라이파
    hash_table_add('이마노 츠루기', 'とうぜんです！')
    hash_table_add('호타루마루', 'はぁーい、隊員やりまーす')
    hash_table_add('아카시 쿠니유키', 'はぁー、自分に「働け」言いますか？参りましたなぁ')
    hash_table_add('미카츠키 무네치카', 'うむ、では参加するか')
    hash_table_add('이치고 히토후리', 'お任せください')
    hash_table_add('카슈 키요미츠', '加州清光、入りまーす')
    hash_table_add('야마토노카미 야스사다', '出番だね、了解！')
    hash_table_add('모노요시 사다무네', 'はい！幸運を運びますね！')
    hash_table_add('호리카와 쿠니히로', 'お手伝いなら任せて！')
    hash_table_add('고코타이', 'はっ……はいっ！')
    hash_table_add('호쵸 토시로', 'ほーい！')

    # print('● 혼마루 첫 모습:')
    # print(hash_table)

    print('● 쿠니유키 일해!:')
    print(hash_table_search('아카시 쿠니유키'))

    # 앗! 야스사다가 수행을 떠났다!
    hash_table_delete('야마토노카미 야스사다')

    # print('● 혼마루 두 번째 모습:')
    # print(hash_table)

    # 돌아왔다!
    hash_table_add('야마토노카미 야스사다', '出番だね。わかった')

    # 수행을 더 보낸다.
    hash_table_delete('호타루마루')
    hash_table_delete('이마노 츠루기')
    hash_table_delete('모노요시 사다무네')
    hash_table_delete('고코타이')

    print('● 미카치 편성!:')
    print(hash_table_search('미카츠키 무네치카'))

    # print('● 혼마루 세 번째 모습:')
    # print(hash_table)
elif SCENARIO_NUMBER == 1:
    hash_table_add('야마토노카미 야스사다', '出番だね、了解！')

    print('● 얏사다~~!!!')
    print(hash_table_search('야마토노카미 야스사다'))
