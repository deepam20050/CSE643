start:-
  write('Elective prediction system'), nl, nl,
  write('Enter Name: '), nl, nl,
  read(Name), nl, nl,
  write('Enter Age: '), nl, nl,
  read(Age), nl, nl,
  write('Enter Branch: '), nl, nl,
  read(Branch), nl, nl,
  write('Enter Semester: '), nl, nl,
  read(Sem), nl, nl,
  careerOptions.

branch('CSE', 'Research', ['AD', 'CMPT', 'ML']).
branch('CSE', 'ML', ['ML', 'SML', 'DMG']).
branch('CSE', 'SDE', ['CldC', 'MAD', 'GDD']).
branch('CSE', 'Cyber', ['FCS', 'NSS-II', 'PSOSM']).
branch('CSE', 'Startup', ['MB', 'GMT', 'FF']).

branch('CSAI', 'Research', ['AI', 'IIS', 'IAI']).
branch('CSAI', 'ML', ['AOMML', 'BML', 'MLRC']).
branch('CSAI', 'SDE', ['CG', 'PN', 'MC']).
branch('CSAI', 'Cyber', ['FCS', 'NSS-II', 'TMC']).
branch('CSAI', 'Startup', ['BA', 'KCES', 'CCS']).

branch('CSAM', 'Research', ['IML', 'TNT', 'LO']).
branch('CSAM', 'ML', ['SML', 'DL', 'MIV']).
branch('CSAM', 'SDE', ['SDOS', 'CV', '5GN']).
branch('CSAM', 'Cyber', ['TAC', 'ANNT', 'NT']).
branch('CSAM', 'Startup', ['MB', 'VCA', 'FF']).

branch('CSD', 'Research', ['RMSSD', 'MD', 'DSCD']).
branch('CSD', 'ML', ['DHCS', 'ML', 'AML']).
branch('CSD', 'SDE', ['CG', 'RL', 'SML']).
branch('CSD', 'Cyber', ['FCS, CN, CldC']).
branch('CSD', 'Startup', ['FF', 'MB', 'NPTELNOC']).

branch('CSB', 'Research', ['FOMB', 'CBB', 'CM']).
branch('CSB', 'ML', ['ML', 'DMG', 'DSG']).
branch('CSB', 'SDE', ['CA', 'IBC', 'DW']).
branch('CSB', 'Cyber', ['FCS', 'CN', 'MAS']).
branch('CSB', 'Startup', ['FF', 'EF', 'NVP']).

branch('CSSS', 'Research', ['ACV', 'RL', 'IMC']).
branch('CSSS', 'ML', ['AOMML', 'COO', 'ALA']).
branch('CSSS', 'SDE', ['DLM', 'IRob', 'CF']).
branch('CSSS', 'Cyber', ['MEL', 'TSE', 'FCS']).
branch('CSSS', 'Startup', ['MA', 'ECO', 'MD']).

branch('ECE', 'Research', ['RS', 'DSP', 'DHD']).
branch('ECE', 'ML', ['AML', 'RL', 'SNS']).
branch('ECE', 'SDE', ['GDD', 'DAVP', 'CG']).
branch('ECE', 'Cyber', ['CS', 'SEC', 'OCNS']).
branch('ECE', 'Startup', ['Psy', 'FF', 'MB']).

careerOptions:-
  write('Enter which career stream you wish to take up: '), nl, nl,
  write('[1]. Research'), nl, nl,
  write('[2]. Job'), nl, nl,
  write('[3]. Entrepreneurship'), nl, nl,
  read(Option), nl, nl,
  (Option = 1 -> choiceResearch ; 
    (Option = 2 -> choiceJob ;
      choiceEntrepreneurship)).

choiceResearch:-
  write('Have you done BTP ? '), nl, nl,
  read(BTP), nl, nl,
  stateBTP(BTP), nl, nl,
  format('The following electives are suggested for you : ~n'),
  branch(Branch, 'Research', L), nl, nl,
  write(L), nl, nl,
  write('Enter the electives which you have already done in list form'), nl, nl,
  read(Electives), nl, nl,
  subtract(L, Electives, X),
  write('Enter CGPA: '), nl, nl,
  read(Gpa), nl, nl,
  mapGPA(Gpa, GpaMapped),
  format('The following courses are recommended in decreasing order of preference: '), nl, nl,
  (GpaMapped = 2 -> print_list(X) ; write('A suggestion is for a career in research CGPA > 9 is suggested'), nl, nl, reverse(X, [], LL), print_list(LL)), nl, nl.

mapGPA(Gpa, GpaMapped):-
  (Gpa >= 9 -> GpaMapped is 2 ; 
    (Gpa >= 8 -> GpaMapped is 1 ;
      (GpaMapped is 0))).

stateBTP(BTP):-
  BTP = y -> write('Good! Doing a BTP helps a lot in research'); write('It is highly suggested to do a BTP').

choiceJob:-
  format('Enter in list form the core electives in 1st and 2nd year that you have completed ~n'),
  read(Year12), nl, nl,
  subtract(['IP', 'COMM', 'DSA', 'AP', 'OS', 'ADA', 'CN'], Year12, Remaining),
  length(Remaining, Len),
  (Len = 0 -> write('Good! all you fundamental courses are cleared!') ; write('Make sure to finish these courses ASAP before the placement season : '), print_list(Remaining), nl),
  write('Which field do you want to work in ? '), nl,
  write('[1]. ML'), nl,
  write('[2]. SDE'), nl,
  write('[3]. Cyber Security'), nl,
  read(Option),
  (Option = 1 -> choiceML ; 
    (Option = 2 -> choiceSDE ;
      choiceCyberSecurity)).

choiceML:-
  format('The following electives are suggested for you : ~n'),
  branch(Branch, 'ML', L), nl, nl,
  write(L), nl, nl,
  write('Enter the electives which you have already done in list form'), nl, nl,
  read(Electives), nl, nl,
  subtract(L, Electives, X),
  write('Enter CGPA: '), nl, nl,
  read(Gpa), nl, nl,
  mapGPA(Gpa, GpaMapped),
  format('The following courses are recommended in decreasing order of preference: '), nl, nl,
  (GpaMapped >= 1 -> print_list(X) ; reverse(X, [], LL), print_list(LL)), nl, nl.

choiceSDE:-
  format('The following electives are suggested for you : ~n'),
  branch(Branch, 'SDE', L), nl, nl,
  write(L), nl, nl,
  write('Enter the electives which you have already done in list form'), nl, nl,
  read(Electives), nl, nl,
  subtract(L, Electives, X),
  write('Enter CGPA: '), nl, nl,
  read(Gpa), nl, nl,
  mapGPA(Gpa, GpaMapped),
  format('The following courses are recommended in decreasing order of preference: '), nl, nl,
  (GpaMapped >= 1 -> print_list(X) ; reverse(X, [], LL), print_list(LL)), nl, nl.
  
choiceCyberSecurity:-
  format('The following electives are suggested for you : ~n'),
  branch(Branch, 'Cyber', L), nl, nl,
  write(L), nl, nl,
  write('Enter the electives which you have already done in list form'), nl, nl,
  read(Electives), nl, nl,
  subtract(L, Electives, X),
  write('Enter CGPA: '), nl, nl,
  read(Gpa), nl, nl,
  mapGPA(Gpa, GpaMapped),
  format('The following courses are recommended in decreasing order of preference: '), nl, nl,
  (GpaMapped >= 1 -> print_list(X) ; reverse(X, [], LL), print_list(LL)), nl, nl.

choiceEntrepreneurship:-
  format('The following electives are suggested for you : ~n'),
  branch(Branch, 'Startup', L), nl, nl,
  write(L), nl, nl,
  write('Enter the electives which you have already done in list form'), nl, nl,
  read(Electives), nl, nl,
  subtract(L, Electives, X),
  write('Enter CGPA: '), nl, nl,
  read(Gpa), nl, nl,
  mapGPA(Gpa, GpaMapped),
  format('The following courses are recommended in decreasing order of preference: '), nl, nl,
  (GpaMapped >= 1 -> print_list(X) ; reverse(X, [], LL), print_list(LL)), nl, nl.

print_list([]).
print_list([H | T]) :-
  format('~s ', [H]),
  print_list(T).

% Ref : https://slaystudy.com/prolog-program-to-reverse-a-list/?utm_source=rss&utm_medium=rss&utm_campaign=prolog-program-to-reverse-a-list
reverse([], Y, R) :-
  R = Y.
reverse([H|T], Y, R) :-
  reverse(T, [H|Y], R).