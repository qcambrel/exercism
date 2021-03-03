def convert(number):
    rain = ''
    sounds = {
    	3: 'Pling', 
    	5: 'Plang', 
    	7: 'Plong'
    }
    factors = sorted(sounds.keys())
    for factor in factors:
    	if number % factor == 0:
    		rain += sounds[factor]
    return rain if rain else str(number)

