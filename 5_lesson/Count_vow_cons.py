# Task 31: Vowels & Consonants

# Tasks:
# 1. We need to have sequences of consonants and vowels
# 2. then we can iterate over the whole string
# 3. and check each character, whether it is a letter
# 4. and whether it is a consonant
# 5. or a vowel
# 6. The dictionary that keep the counts, should be created before we begin to loop over the sentence. It will have two categories mapped to actual counts, which are at the beginning set to 0.

# 1.
vowels = 'aeiouy'

counts = {'cons':0,'vows':0}

sentence = 'A speech sound that is produced by comparatively open configuration of the vocal tract.'

# 2.
for char in sentence:
    # 3.
    if not char.isalpha():
        continue
    # 4.
    if char.lower() in vowels:
        counts['vows'] += 1
    # 5.
    else:
        counts['cons'] += 1

print('No. consonants: ' + str(counts['cons']) + ' | No. vowels: ' + str(counts['vows']))