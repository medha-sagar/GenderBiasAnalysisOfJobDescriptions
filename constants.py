masculine_keywords = ['active', 'adventurous', 'aggress', 'ambitio', 'analy', 'assert', 'athlet', 'autonom', 'battle', 'boast', 'challeng', 'champion', 'compet', 'confident', 'courag', 'decid', 'decision', 'decisive', 'defend', 'determin', 'domina', 'dominant', 'driven', 'fearless', 'fight', 'force', 'greedy', 'head strong', 'headstrong', 'hierarch', 'hostil', 'impulsive', 'independen', 'individual', 'intellect', 'lead', 'logic', 'objective', 'opinion', 'outspoken', 'persist', 'principle', 'reckless', 'self confiden', 'self relian', 'self sufficien', 'selfconfiden', 'selfrelian', 'selfsufficien', 'stubborn', 'superior', 'unreasonab', 'capable', 'certain', 'focus', 'benefit', 'trust ', 'trusting', 'acceptance ', 'accepting', 'appreciative ', 'appreciation', 'admire ', 'admiration', 'approval', 'encouragement', 'power', 'strenght', 'competency ', 'competence', 'efficient ', 'efficiency', 'achievement', 'honor', 'pride', 'dignity', 'solution ', 'solutions', 'success', 'skills', 'autonomy', 'love', 'serve', 'support', 'give ', 'giving', 'provide', 'devoted', 'fulfill', 'caretaker', 'space', 'useful', 'rational', 'strategy ', 'strategic', 'plan ', 'planning', 'analytic ', 'analytical', 'reasonable', 'consider', 'analyse ', 'analysing', 'believe', 'opinion', 'suggestion', 'think', 'prove themselves', 'achieve results', 'feel good about himself', 'doing things by himself', 'loving acceptance', 'feeling needed', 'someone to serve', 'good enough', 'fulfill others', 'silent acceptance', 'comforting love', 'common sense', 'point of view', 'active', 'adventurous', 'aggress', 'ambitio', 'analy', 'assert', 'athlet', 'autonom', 'boast', 'challeng', 'compet', 'confident', 'courag', 'decide', 'decisive', 'decision', 'determin', 'dominant', 'domina', 'force', 'greedy', 'headstrong', 'hierarch', 'hostil', 'implusive', 'independen', 'individual', 'intellect', 'lead', 'logic', 'masculine', 'objective', 'opinion', 'outspoken', 'persist', 'principle', 'reckless', 'stubborn', 'superior', 'self confiden', 'self sufficien', 'self relian']
feminine_keywords = ['agree', 'affectionate', 'child', 'cheer', 'collab', 'commit', 'communal', 'compassion', 'connect', 'considerate', 'cooperat', 'co operat', 'depend', 'emotiona', 'empath', 'feel', 'flatterable', 'gentle', 'honest', 'interdependen', 'interpersona', 'inter personal', 'inter dependen', 'inter persona', 'kind', 'kinship', 'loyal', 'modesty', 'nag', 'nurtur', 'pleasant', 'polite', 'quiet', 'respon', 'sensitiv', 'submissive', 'support', 'sympath', 'tender', 'together', 'trust', 'understand', 'warm', 'whin', 'enthusias', 'inclusive', 'yield', 'share', 'sharin', 'affectionate', 'child', 'cheer', 'commit', 'communal', 'compassion', 'connect', 'considerate', 'cooperat', 'depend', 'emotiona', 'empath', 'feminine', 'flatterable', 'gentle', 'honest', 'interdependen', 'interpersona', 'kindkinship', 'loyal', 'modesty', 'nag', 'nurtur', 'pleasant', 'polite', 'quiet', 'respon', 'sensitiv', 'submissive', 'support', 'sympath', 'tender', 'together', 'trust', 'understand', 'warm', 'whin', 'yield', 'ease', 'permission', 'kindness', 'appreciation', 'caring', 'respect', 'devotion', 'validation', 'reassurance', 'respectful', 'love', 'communication', 'beauty', 'relationships', 'helping', 'sharing', 'relating', 'harmony', 'community', 'talking', 'intimate', 'life', 'healing', 'growth', 'intuitive', 'companionship', 'receive ', 'receiving', 'cherished', 'creativity', 'reassurance', 'worthy', 'supported ', 'supporting', 'nurture ', 'nurturing ', 'nurtured', 'feel', 'emotion']
superlative_keywords = ['expert', 'perfection', 'rockstar', 'specialist', 'authority', 'pundit', 'oracle', 'resource person', 'adept', 'maestro', 'virtuoso', 'master', 'past master', 'professional', 'genius', 'wizard', 'connoisseur', 'aficionado', 'cognoscenti', 'cognoscente', 'doyen', 'savant', 'ace', 'buff', 'ninja', 'pro', 'whizz', 'hotshot', 'old hand', 'alpha geek', 'dab hand', 'maven', 'crackerjack']
genders = ['Male', 'Female']
manager_keywords = ['senior', 'head', 'director', 'lead', 'president', 'chairmen', 'chief']

base_path = "data/cityofla/CityofLA/Job_Bulletins/"
structured_path = "data/cityofla/CityofLA/Additional_Data/structured_file.csv"
titles = open("data/cityofla/CityofLA/Additional_Data/job_titles.csv").read().strip().split("\n")