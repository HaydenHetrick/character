def main():
    character_name = ''
    character_id = ''
    character_level = 0
    character_loot = 0.0

    boss_name = ''
    boss_id = ''
    boss_level = 0
    boss_hp = 0.0
    boss_attack_damage = 0.0

    print('Character:')
    character_name = input('Enter the hero name: ')
    character_id = input('Enter the character ID number: ')
    character_level = int(input('Enter the hero level: '))
    character_loot = float(input('Enter the hero loot value: '))

    hero = Character(character_name, character_id, character_level, character_loot)

    print('')
    print('Boss:')
    boss_name = input('Enter the boss name: ')
    boss_id = input('Enter the boss ID number: ')
    boss_level = int(input('Enter the boss level: '))
    boss_hp = float(input('Enter the boss hp: '))
    boss_attack_damage = float(input('Enter the boss attack damage: '))

    boss = boss(boss_name, boss_id, boss_level, boss_hp, boss_attack_damage)

    print('')
    print('Character:')
    print(f'Name: {hero.get_name()}')
    print(f'ID number: {hero.get_id_number()}')
    print(f'Level: {hero.get_level()}')
    print(f'Loot: ${hero.get_loot():,.2f}')

    print('')
    print('Boss information: ')
    print(f'Name: {boss.get_name()}')
    print(f'ID number: {boss.get_id_number()}')
    print(f'Level: {boss.get_level()}')
    print(f'HP: {boss.get_hp()}')
    print(f'Attack Damage: {boss.get_attack_damage()}')
    print(f'Lifespan: {boss.get_lifespan():,.2f} attacks')


if __name__ == '__main__':
    main()
