from durable.lang import *

#---------------------------------------------------------------------------------------
# Triggered by 'interests' fact
# It gets triggered by the entered interest of courses and the current grade of the user. 
#---------------------------------------------------------------------------------------

with ruleset('interests'):
	
	@when_all((m.interest == 'machine learning') & (m.grade >= 7))
	def machinelearning(c):
		c.assert_fact('basic courses',{'choice':'machine_learning'})	
		c.assert_fact('courses',{'field':'machineLearning'})
		c.assert_fact('activities',{'club':'robotics'})
	
	@when_all((m.interest == 'deep learning') & (m.grade >= 8))
	def deeplearning(c):	
		c.assert_fact('interests',{'interest':'machine learning','grade':grade})
		c.assert_fact('courses',{'field':'deepLearning'})
			
		
	@when_all((m.interest == 'data engineering') & (m.grade >= 6))
	def datangineering(c):
		c.assert_fact('basic courses',{'choice':'data_engineering'})	
		c.assert_fact('courses',{'field':'dataEngineering'})	

	@when_all((m.interest == 'software development') & (m.grade >= 6))
	def softwaredevelopment(c):
		c.assert_fact('basic courses',{'choice':'software_development'})	
		c.assert_fact('courses',{'field':'softwareDevelopment'})
		c.assert_fact('activities',{'club':'softwaredevelopment'})	
	
	@when_all((m.interest == 'computer vision') & (m.grade >= 8))
	def computervision(c):
		c.assert_fact('basic courses',{'choice':'computer_vision'})
		c.assert_fact('courses',{'field':'computerVision'})
		c.assert_fact('activities',{'club':'robotics'})
	
	@when_all((m.interest == 'algorithms') & (m.grade >= 7))
	def algorithms(c):
		c.assert_fact('basic courses',{'choice':'algorithms'})	
		c.assert_fact('courses',{'field':'algorithms'})
		c.assert_fact('activities',{'club':'coding'})

	@when_all((m.interest == 'animation') & (m.grade >= 7))
	def animation(c):
		c.assert_fact('basic courses',{'choice':'animation'})	
		c.assert_fact('courses',{'field':'animation'})
		c.assert_fact('activities',{'club':'design'})
	
	@when_all((m.interest == 'speechaudio') & (m.grade >= 7))
	def speechaudio(c):
		c.assert_fact('courses',{'field':'speechAudio'})
	
	@when_all((m.interest == 'cybersecurity') & (m.grade >= 8))
	def cybersecurity(c):
		c.assert_fact('basic courses',{'choice':'cyber_security'})
		c.assert_fact('courses',{'field':'cyberSecurity'})
		c.assert_fact('activities',{'club':'security'})
	
	@when_all((m.interest == 'wirelesscommunication') & (m.grade >= 7))
	def wirelesscommunication(c):
		c.assert_fact('basic courses',{'choice':'wireless_communication'})
		c.assert_fact('courses',{'field':'wirelessCommunication'})
		c.assert_fact('activities',{'club':'electroholics'})
	
	@when_all((m.interest == 'vlsi') & (m.grade >= 6))
	def vlsi(c):
		c.assert_fact('courses',{'field':'vlsi'})
		c.assert_fact('activities',{'club':'electroholics'})
	
	@when_all((m.interest == 'csp') & (m.grade >= 6))
	def csp(c):
		c.assert_fact('courses',{'field':'csp'})
		c.assert_fact('activities',{'club':'electroholics'})
	

	@when_all((m.interest == 'bio') & (m.grade >= 6))
	def bio(c):
		c.assert_fact('basic courses',{'choice':'bio'})
		c.assert_fact('courses',{'field':'bio'})
		c.assert_fact('activities',{'club':'bio'})
	
	@when_all((m.interest == 'psychology') & (m.grade >= 6))
	def psychology(c):
		c.assert_fact('courses',{'field':'psychology'})
		c.assert_fact('activities',{'club':'philosophy'})
	
	
	@when_all(+m.subject)
	def output(c):
		print('Fact: {0} {1} {2}'.format(c.m.subject, c.m.predicate, c.m.object))

#---------------------------------------------------------------------------------------
# Triggered by 'basic courses' fact
# It gets triggered by the choice of subject entered above and calling the respective 
# foundation courses available for that interest 
#---------------------------------------------------------------------------------------
with ruleset('basic courses'):
	
	@when_all((m.choice == 'machine_learning'))
	def machinelearning(e):
		e.assert_fact({'subject':'Choose','predicate':'Foundation Course - ','object':'Probability and Statistics'})
		e.assert_fact({'subject':'Choose','predicate':'Foundation Course - ','object':'Linear Algebra'})

	@when_all((m.choice == 'data_engineering'))
	def dataengineering(e):
		e.assert_fact({'subject':'Choose','predicate':'Foundation Course - ','object':'Fundamentals of Database Management Systems'})
		e.assert_fact({'subject':'Choose','predicate':'Foundation Course - ','object':'Data Structure and Algorithms'})
	
	@when_all((m.choice == 'software_development'))
	def softwaredevelopment(e):
		e.assert_fact({'subject':'Choose','predicate':'Foundation Course - ','object':'Advance Programming'})
		e.assert_fact({'subject':'Choose','predicate':'Foundation Course - ','object':'Object Oriented Programming and Design'})
		e.assert_fact({'subject':'Choose','predicate':'Foundation Course - ','object':'Analysis and Design of Algorithms'})
	
	@when_all((m.choice == 'computer_vision'))
	def computervision(e):
		e.assert_fact({'subject':'Choose','predicate':'Foundation Course - ','object':'Digital Image Processing'})
		e.assert_fact({'subject':'Choose','predicate':'Foundation Course - ','object':'Mathematics - I'})

	@when_all((m.choice == 'algorithms'))
	def algorithms(e):
		e.assert_fact({'subject':'Choose','predicate':'Foundation Course - ','object':'Data Structures and Algorithms'})
		e.assert_fact({'subject':'Choose','predicate':'Foundation Course - ','object':'Analysis and Design of Algorithms'})

	@when_all((m.choice == 'animation'))
	def animations(e):
		e.assert_fact({'subject':'Choose','predicate':'Foundation Course - ','object':'Design Drawing and Visualization'})
	
	@when_all((m.choice == 'cyber_security'))
	def cybersecurity(e):
		e.assert_fact({'subject':'Choose','predicate':'Foundation Course - ','object':'Foundations of Computer Security'})

	@when_all((m.choice == 'wireless_communication'))
	def wirelesscommunication(e):
		e.assert_fact({'subject':'Choose','predicate':'Foundation Course - ','object':'Principles of Communication Sysytem'})
		e.assert_fact({'subject':'Choose','predicate':'Foundation Course - ','object':'Operating Systems'})

	@when_all((m.choice == 'bio'))
	def bio(e):
		e.assert_fact({'subject':'Choose','predicate':'Foundation Course - ','object':'Introduction to Mathematical Biology'})
		e.assert_fact({'subject':'Choose','predicate':'Foundation Course - ','object':'Foundations of Modern Biology '})


	@when_all(+m.subject)
	def output(e):
		print('Fact: {0} {1} {2}'.format(e.m.subject, e.m.predicate, e.m.object))

#---------------------------------------------------------------------------------------
# Triggered by 'courses' fact
# It gets triggered by the choice of subject entered above and calling the respective 
# core/elective courses available for that interest 
#---------------------------------------------------------------------------------------
with ruleset('courses'):
	
	@when_all((m.field == 'machineLearning'))
	def machinelearning(d):
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Statistical Machine Learning'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Natural Language Processing'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Artificial Intelligence'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Bayesian Machine Learning'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Reinforcement Learning'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Machine Learning'})
	
	@when_all((m.field == 'deepLearning'))
	def deeplearning(d):
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Advanced Machine Learning'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Computer Vision'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Theories of Deep Learning'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Deep Learning'})
	
	@when_all((m.field == 'dataEngineering'))
	def dataengineering(d):
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Machine Learning'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Information Retrieval'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Natural Language Processing'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Big Data analytics'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Semantic Web'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Collaborative Filtering'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Data Mining'})

	@when_all((m.field == 'softwareDevelopment'))
	def softwaredevelopment(d):
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Mobile Computing'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Software Development using Open Source '})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Topics in Software Engineering: AI in SE '})

	@when_all((m.field == 'computerVision'))
	def computervision(d):
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Human Computer Ineraction'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Biomedical Image Processing'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Advance Computer Vision'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Computer Vision'})	
	
	@when_all((m.field == 'algorithms'))
	def algorithms(d):
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Modern Algorithm Design'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Randomized Algorithms'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Algorithms in Computational Biology'})	
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Program Verification and Analysis'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Introduction to Graduate Algorithms'})
		
	@when_all((m.field == 'animation'))
	def animation(d):
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Introduction to 3D Character Animation'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Wearable Applications, Research, Devices, Interactions '})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Introduction to 2D Animation'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Design of Interactive Systems'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Advanced Topics in Human-Centered Computing'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':' Introduction to 3D Production Design for Animation and Games'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Game Design and Development'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Film Making and Radio Podcasting'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Animations & Graphics'})
	
	@when_all((m.field == 'speechAudio'))
	def speechaudio(d):
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Digital Audio & Video Production Workflow'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Digital Audio '})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Fundamentals of Audio for Engineers'})

	@when_all((m.field == 'cyberSecurity'))
	def cybersecurity(d):
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Multimedia Security'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Privacy and Security in Online Social Media'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Network Security'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Topics in Adaptive Cybersecurity'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Speech and Audio Processing'})	
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Networks and System Security'})	

	@when_all((m.field == 'wirelessCommunication'))
	def wirelesscommunication(d):
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Optical Communications Systems'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Distributed Systems: Concepts and Design'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Foundations of Parallel Programing'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Wireless System Implementation'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Wireless Communication: Evolution from 3G to 5G'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Wireless Network'})	

	@when_all((m.field == 'vlsi'))
	def vlsi(d):
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Solid State Devices'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'RF Circuit Design'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Probability and Random Processes'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Integrated Circuit Fabrication'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Low Voltage Circuit Design'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Digital VLSI Design'})	

	@when_all((m.field == 'csp'))
	def csp(d):
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Probability Theory and Random Processes'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Principles of Digital Communication System'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Statistical Signal Processing'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Low Voltage Circuit Design'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Optical Communications Systems'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Advanced Embedded Logic Design'})	

	@when_all((m.field == 'bio'))
	def bio(d):
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Computing for Medicine'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Algorithms in Computational Biology'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Big Data Mining in Healthcare'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Computational Gastronomy'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Machine Learning for Biomedical Applications'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Network Biology'})	
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Computer Aided Drug Design'})	

	@when_all((m.field == 'psychology'))
	def psychology(d):
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Cognitive Psychology'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'3 Sociology of India: Themes and Perspectives'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Philosophy of Mind'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Computer, Information Ethics and Society'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Neuroscience of Decision Making'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Philosophy of Technology'})
		d.assert_fact({'subject':'Choose','predicate':'Elective Course - ','object':'Social Psychology'})	

	@when_all(+m.subject)
	def output(d):
		print('Fact: {0} {1} {2}'.format(d.m.subject, d.m.predicate, d.m.object))

#---------------------------------------------------------------------------------------
# Triggered by 'activities' fact
# It gets triggered by the choice of subject entered above and calling the respective 
# technical clubs available for that interest 
# Non technical clubs as extra curricular ciurses are being called by asking the 
# further interest of the user.
#---------------------------------------------------------------------------------------
with ruleset('activities'):
	
	@when_all((m.club == 'astronomy'))
	def astronomy(f):
		f.assert_fact({'subject':'NonTechnical','predicate':'Club','object':'Astrobuts :- Astronomy Club'})
	
	@when_all((m.club == 'bio'))
	def bio(f):
		f.assert_fact({'subject':'Technical','predicate':'Club','object':'BioBytes :- Computational Biology'})
		f.assert_fact({'subject':'Technical','predicate':'Club','object':'Salt N Pepper :- Cuisines Promotion Club'})
	
	@when_all((m.club == 'robotics'))
	def robotics(f):
		f.assert_fact({'subject':'Technical','predicate':'Club','object':'CyBorg :- Robotics Club'})
	
	@when_all((m.club == 'security'))
	def security(f):
		f.assert_fact({'subject':'Technical','predicate':'Club','object':'d4rkc0de :- Security Enthusiasts Club'})

	@when_all((m.club == 'design'))
	def design(f):
		f.assert_fact({'subject':'Technical','predicate':'Club','object':'DesignHub :- Design Club'})
	
	@when_all((m.club == 'electroholics'))
	def electroholics(f):
		f.assert_fact({'subject':'Technical','predicate':'Club','object':'Electroholics :- Hardware enthusiasts Club'})

	@when_all((m.club == 'coding'))
	def coding(f):
		f.assert_fact({'subject':'Technical','predicate':'Club','object':'Foobar :- Competitive Programming Club'})
	
	@when_all((m.club == 'softwaredevelopment'))
	def softwaredevelopment(f):
		f.assert_fact({'subject':'Technical','predicate':'Club','object':'BYLD :- Software Development Club'})
	
	@when_all((m.club == 'audio'))
	def audio(f):
		f.assert_fact({'subject':'NonTechnical','predicate':'Club','object':'Audiobytes :- Music Society'})
	
	@when_all((m.club == 'literature'))
	def literature(f):
		f.assert_fact({'subject':'NonTechnical','predicate':'Club','object':'LitSoc :- Literary, Debating and Anime Society'})
	
	@when_all((m.club == 'theatre'))
	def theatre(f):
		f.assert_fact({'subject':'NonTechnical','predicate':'Club','object':'Machaan :- Drama Club'})
	
	@when_all((m.club == 'dance'))
	def dance(f):
		f.assert_fact({'subject':'NonTechnical','predicate':'Club','object':'MadToes :- Dance Society'})	
	
	@when_all((m.club == 'standup'))
	def standup(f):
		f.assert_fact({'subject':'NonTechnical','predicate':'Club','object':'MicDrop:- Stand-up Comedy Club'})

	@when_all((m.club == 'photography'))
	def photography(f):
		f.assert_fact({'subject':'NonTechnical','predicate':'Club','object':'Tasveer :- Photography Club'})
	
	@when_all((m.club == 'finance'))
	def finance(f):
		f.assert_fact({'subject':'NonTechnical','predicate':'Club','object':'Finnexia :- Finance Club'})

	@when_all((m.club == 'art'))
	def art(f):
		f.assert_fact({'subject':'NonTechnical','predicate':'Club','object':'Meraki :- Art Society'})
	
	@when_all((m.club == 'fashion'))
	def fashion(f):
		f.assert_fact({'subject':'NonTechnical','predicate':'Club','object':'Muse :- Fashion Club'})
	
	@when_all((m.club == 'philosophy'))
	def philosophy(f):
		f.assert_fact({'subject':'NonTechnical','predicate':'Club','object':'Pilosoc :- Philosophy Club'})

	@when_all(+m.subject)
	def output(f):
		print('Fact: {0} {1} {2}'.format(f.m.subject, f.m.predicate, f.m.object))


#Creating the dictionary which stores the indexes of the interest of courses available
interest_dict = {1:'machine learning', 2:'deep learning', 3:'data engineering', 4:'software development', 5:'computer vision', 6:'algorithms', 7:'animation', 8:'speechaudio', 9:'cybersecurity', 10:'wirelesscommunication', 11:'vlsi', 12:'csp', 13:'bio', 14:'psychology' }

#Creating the dictionary which stores the indexes of the non technical interest of extra curricular activities available
extracurricular_dict = {1:'astronomy', 2:'audio', 3:'literature', 4:'theatre', 5:'dance', 6:'standup', 7:'photography', 8:'finance', 9:'art', 10:'fashion'}

#Starting the program
print('Designed By:-')
print('Name - Shreya Goel \t\t Roll No. - MT20054')
print('Welcome to Courses and Curricular Activities Guide System!')
print('We will guide you the best courses that can be chosen according to the your interest and grade')
print()

#Input the grade from the student which should be between 1 to 10.
while(True):
	grade = int(float(input('Enter your current CGPA/Grade in the range of 1-10 ')))
	if (grade >= 1 and grade <= 10) :
		break
	else:
		print('You did not enter the correct grade. Please enter again!')
		print()

print()
print('Choose the best interest that suits you! Enter the index of the choice. ')
print()
print()

#Printing the available interests for Courses and Technical Club 
print('Available Interests for Courses and Technical Clubs: ')
print()
print(' 1. Machine Learning \n 2. Deep Learning \n 3. Data Engineering \n 4. Software Development/ Android Development/ Web Development \n 5. Computer Vision \n 6. Algorithms Development and Analysis \n 7. Animation and Graphics \n 8. Speech and Audio Processing \n 9. Cyber and Network Security \n 10. Wireless Communications \n 11. VLSI Design Related Area \n 12. Communication and Signal Processing \n 13. Computational Biology \n 14. Psychology/Social/Philosophy Related Area ')
print()

#Input the interest for the course by using the index of the choice.
while(True):
	choice_interest = int(float(input('Enter the index of the interest that suits you! ')))
	if(choice_interest >= 1 and choice_interest <= 14):
		interest_value = interest_dict[choice_interest]
		break

	else:
		print("Invalid Choice Entered! Enter again! ")
		print()

print()
print()

#Printing the available interests for Extra Curricular Activities - Non Technical Club 
print('Available Interests for Non Technical Clubs: ')
print()
print(' 1. Astronomy \n 2. Audio/Music  \n 3. Literary, Debating and Anime  \n 4. Theatre/Drama \n 5. Dance \n 6. Stand up Comedy \n 7. Photography \n 8. Finance \n 9. Art \n 10. Fashion')
print()

#Input the interest for the extra curricular activity by using the index of the choice.
while(True):
	choice_interest_1 = int(float(input('Enter the index of the interest that suits you! ')))
	print()
	if(choice_interest_1 >= 1 and choice_interest_1 <= 10):
		interest_value_1 = extracurricular_dict[choice_interest_1]
		print()
		print('Displaying the Courses and the Curricular Activities Club! ')
		print()
		#Calling the course facts on the basis of input by the student
		try:
			assert_fact('interests', {'interest':interest_value, 'grade':grade})

		except BaseException as e:
			print('Your grade does not satisfy the criteria for taking courses based on your Interest! You need to work hard on grade!' )
		
		#Calling the extra curricular activity facts on the basis of input by the student
		try:
			assert_fact('activities', {'club':interest_value_1})
		
		except BaseException as e:
			print('Your Interest does not satisfy the Non technical Clubs Available in IIITD!' )
		break
	
	else:
		print("Invalid Choice Entered! Enter again! ")
		print()