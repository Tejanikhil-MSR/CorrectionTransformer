# We need to more concentrate on substitutions

'''
1. Donot touch '్' at any situation. It is the binding character for many consonant clusters.
2. Types of stacking in character :
- Simple Stacking (A reduced-size version of the 2nd consonant has any headstroke removed and is simply positioned below the 1st)
   - ద్ద = 'ద' + '్' + 'ద'
   - థ్థ = 'థ' + '్' + 'థ'
   - ట్ట = ట + '్' + 'ట'
   - గ్గ = 'గ' + '్' + 'గ'
   - డ్డ = 'డ' + '్' + 'డ'
- Stacking with transformation (An alternative shape for the 2nd consonant is positioned directly below the 1st)
    - త్త = 'త' + '్' + 'త'
    - ర్ర = 'ర' + '్' + 'ర'
    - ల్ల = 'ల' + '్' + 'ల'
- Conjoined with reduced, spacing form (The shape of the 2nd consonant is transformed into something that sits alongside the 1st, but extends above and below the baseline)
    - న్న = 'న' + '్' + 'న'
    - మ్మ = 'మ' + '్' + 'మ'
    - స్స = 'స' + '్' + 'స'
    - క్క = 'క' + '్' + 'క'
    - య్య = 'య' + '్' + 'య'
    - బ్బ = 'బ' + '్' + 'బ'
    - శ్శ = 'శ' + '్' + 'శ'
- Reph form ()
    - గూర్చి = 'గ' + 'ూ' + 'ర' + '్' + 'చ' + 'ి' (r + chi = rchi)
    - 'య' + 'ి' = 'యి'
'''

StackingReplacements = { # replacing the consonants after '్'

    'త': ['ల'], # త్త → త్ల, త  
    'ల': ['త', 'గ', 'ధ'],
    
    'ప': ['వ', 'స', 'న', 'య'], # గ్ప → గ్వ, గ్స, గ  
    'వ': ['ప', 'చ', 'య'],
    'స': ['ప', 'వ', 'చ', 'న'],

    'డ': ['ధ', 'ద'], # గ్డ → గ్ధ, గ  
    'ధ': ['డ', 'ద', 'గ', 'ల'],
    'ద': ['డ', 'ధ', ' '],

    'గ': ['ధ', 'ల', 'ఠ'], # ల్గ → ల్ధ, ల్ల, ల  
    'ఠ' : ['గ', 'ల'],

    'చ': ['వ', 'స'], # చ్చ → చ్వ, చ్స  

    'న': ['ప', 'వ'], # న్న → న్ప, న్వ, న

    'శ': ['మ'], # శ్క → శ్మ, శ
    'మ': ['శ'],

    'య' : ['వ']
}

Diacritic_replacements = {
    'ొ': ['ా', 'ో', 'ౌ', 'ె'],
    'ో': ['ా', 'ొ', 'ౌ', 'ే'],
    'ౌ': ['ా', 'ో', 'ొ', 'ే'],
    'ె': ['ి', 'ొ', 'ా'],
    'ి': ['ె', 'ీ', 'ే', 'ై'],
    'ీ': ['ి', 'ే'],
    'ే': ['ి', 'ీ', 'ె', 'ో', 'ౌ'],
    'ై': ['ి', 'ె'],
    'ు': ['ృ', 'ౄ', 'ూ'],
    'ూ': ['ౄ', 'ు'],
    'ృ': ['ు', 'ౄ'],
    'ౄ': ['ు', 'ూ', 'ృ'],
    'ా': ['ొ', 'ో', 'ౌ', 'ె', 'ే'],
}


SimpleCharacterReplacements = { # Direct consonant replacement
       
    'ప': ['స', 'వ', 'న', 'ష', 'ఫ'],
    'ఫ' : ['ప'],
    'స': ['ప'], 'వ': ['ప', 'ష'], 'న': ['ప'],
    
    'ధ': ['ద'],
    'ద': ['ధ', 'ల', 'థ', 'డ'],
    'డ': ['ద', 'త', 'ఢ'],

    'ఘ' : ['ఝ'],
    'ఝ' : ['ఘ'],

    'ల': ['ద'],

    'థ': ['ద'],

    'గ': ['ర'],
    'ర': ['గ', 'ల'],

    'బ': ['భ'],
    'భ': ['బ'],

    'మ': ['య'],
    'య': ['మ'],

    'చ': ['త'],
    'త': ['చ'],

    'ఙ': ['జ'],
    'జ': ['ఙ'],

}
