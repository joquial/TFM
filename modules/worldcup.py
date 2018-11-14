def function(match, category, park, plate):
    result = []
    if park == 'Yes':
        if match == 'Groups1':
            date = '2018/11/05'
        elif match == 'Groups2':
            date = '2018/11/06'
        elif match == 'Quarterfinals':
            date = '2018/11/10'
        elif match == 'Semifinals':
            date = '2018/11/13'
        if category == 'Category 1':
            Gate = 2
        elif category == 'Category 2':
            Gate = 2
        elif category == 'Category 3':
            Gate = 1
        elif category == 'Category 4':
            Gate = 1
        elif category == 'Category 5':
            Gate = 3
        
        result = [{'date':date, 'Gate':Gate, 'Plate Number':plate}]
        return result;
    else:
        return result;


