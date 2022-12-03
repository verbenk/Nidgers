import os

print('іі всім пріет тсе опитуання')
answer=input('Хоч зіграти???? (yes/no) :')
score=0
total_questions=5

if answer.lower()=='yes':
    answer=input('Питання 1: як називаятся мова програмування на якій написаний цей код підсказка(перемішані літери) onhytp :')
    if answer.lower()=='python':
        score += 1
        print('молодець! + 1 бал')
    else:
        print('неправильно :(')


    answer=input('Завдвння 2: тобі подобаєтся комп`ютерна академія ШАГ? (yes/no):  ')
    if answer.lower()=='yes':
        score += 1
        print('Молодець + 1 балл!!')
    else:
        print('еррор 404 :(')

    answer=input('Завдання 3: знайди та напиши неправильнонаписане слово : hello!,  desk, taost , mark, world:')
    if answer.lower()=='toast':
        score += 1
        print('молодець! + 1 бал')
    else:
        print('неправильно :(')

    answer = input('Завдвння 4: напиши на англ мові, (слово на українській, перемішані букви)(діняа): ')
    if answer.lower() == 'hope':
        score += 1
        print('Молодець + 1 балл!!')
    else:
        print('ні :(')

    answer = input('Завдвння 5: переведи слово кисень :  ')
    if answer.lower() == 'oxygen':
        score += 1
        print('Молодець + 1 балл!!')
    else:
        print('брехня :(')

    answer = input('Завдвння 6: чи правда шо 2+2=5: (yes/no) ')
    if answer.lower() == 'no':
        score += 1
        print('Молодець + 1 балл!!')
    else:
        print('ні :(')

    answer = input('Завдa'
                   'ння 7: яке в тебе виходить слово ')
    if answer.lower() == 'python':
        score += 1
        print('Молодець + 1 балл!!')
    else:
        print('ні :(')

    answer = input('Завдвння 8: Чи дозволяє Python програмувати у структурованому стилі? (yes/no) ')
    if answer.lower() == 'yes':
        score += 1
        print('Молодець + 1 балл!!')
    else:
        print('ні :(')

    answer = input('Завдвння 9: чи Python має вбудовану підтримку для обробки обєктів JSON. (yes/no) ')
    if answer.lower() == 'yes':
        score += 1
        print('Молодець + 1 балл!!')
    else:
        print('ні :(')

    answer = input('Завдвння 10:  Python не працює на декількох платформах(вінда, лінукс, мак) без будь-яких змін (True/False) ')
    if answer.lower() == 'False':
        score += 1
        print('Молодець + 1 балл!!')
    else:
        print('ні :(')

    answer = input(
        'Завдвння 11:  як записати *більше  або дорівнює*  ')
    if answer.lower() == '>=':
        score += 1
        print('Молодець + 1 балл!!')
    else:
        print('ні :(')

    answer = input(
        'Завдвння 11:  чи можна командою __cake__ призвати торт!?!?!?! (True/Fals) ')
    if answer.lower() == 'True':
        score += 1
        print('Молодець + 1 балл!!')
    else:
        print('ні :(')


print('   ')

print('дякую за участь і твій результат  -  ',score,"/12")
print('   ')
print('Допобачення!!!')

os.system('python main.py')