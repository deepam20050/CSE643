parse:-
  open('/home/deepam/Desktop/Courses/CSE643/Assignment 5/facts.txt', read, S),
  read_file(S, LL),
  close(S),
  genFFacts(LL).

start:-
	elective(_),
	genList(LL), nl,
	write('Recommended electives are: '), nl, nl,
	sort(LL, Ans),
  print_list(Ans).

% ------- PROLOG HELPER FUNCTIONS -------
genFFacts([H | T]) :- ((H == end_of_file) -> genFFacts(T) ; assert(H), genFFacts(T)).
genFFacts([]).

genList([H | T]):- retract(recommend(H)), genList(T).
genList([]).

% sort in ascending order without deleting duplicates
mysort(List, Result) :- sort(0, @=<, List, Result).

% join two lists
join(List, X, Result) :- append(List, X, Result).

% to check whether element belongs to list
member(X, [X | _]).
member(X, [_ | T]) :- member(X, T).

% to concatenate lists
concatenate([], L, L).
concatenate([E | L1], L2, [E | L3]) :- concatenate(L1, L2, L3).

genpaths([Curr | Path], MorePaths) :-
  findall([To, Curr | Path], (dist(Curr, To, _), \+ member(To, Path)), MorePaths).

% print list
print_list([]).
print_list([H | T]) :-
  format('~s ', [H]),
  print_list(T).

% attach at the front
attach_front(L, X, [X | L]).

askq(Ques) :- (yes(Ques) -> true ; (no(Ques) -> fail ; query(Ques))).

query(QQQ) :-
	format('~w ?',[QQQ]), read(Ans), ((Ans == yes ; Ans == y) -> assert(yes(QQQ)) ; assert(no(QQQ)), fail).

% sort list for best first and A*
sort_list(L, L, _).
sort_list(L, L2, Dest) :- predicate(L, L1, Dest), !, sort_list(L1, L2, Dest).

% predicate to sort based on heuristic
predicate([[H1 | H2], [HH1 | HH2] | T], [[HH1 | HH2], [H1 | H2] | T], Dest) :- h(H1, Dest, Dist1), h(HH1, Dest, Dist2), Dist1 > Dist2.
predicate([H | T], [H | T2], Dest) :- predicate(T, T2, Dest).

% Ref : https://stackoverflow.com/a/4805931
read_file(SS, []) :-
  at_end_of_stream(SS).
read_file(SS, [H | T]) :-
  \+ at_end_of_stream(SS),
  read(SS, H),
  read_file(SS, T).

% ------- PROLOG HELPER FUNCTIONS END -------

elective('TOC') :- toc, fail.
elective('AAG') :- aag, fail.
elective('ML') :- ml, fail.
elective('DL') :- dl, fail.
elective('ADA') :- ada, fail.
elective('AP') :- ap, fail.
elective('FCS') :- fcs, fail.
elective('AC') :- ac, fail.
elective('MB') :- mb, fail.
elective('FF') :- ff, fail.
elective('NONE').

toc :-
  retract(res(R)),
  assert(res(R)),
  (R == yes -> true ; fail),
  askq('automata'),
  assert(recommend('TOC')).

aag :-
  retract(res(R)),
  assert(res(R)),
  (R == yes -> true ; fail),
  askq('algos'),
  assert(recommend('AAG')).

ml :-
  retract(ml(M)),
  assert(ml(M)),
  (M == yes -> true ; fail),
  askq('datascience'),
  assert(recommend('ML')).

dl :-
  retract(ml(M)),
  assert(ml(M)),
  (M == yes -> true ; fail),
  askq('datascience'),
  assert(recommend('DL')).

ada :-
  retract(sde(S)),
  assert(sde(S)),
  (S == yes -> true ; fail),
  askq('cp'),
  askq('coding'),
  assert(recommend('ADA')).

ap :-
  retract(sde(S)),
  assert(sde(S)),
  (S == yes -> true ; fail),
  askq('oop'),
  assert(recommend('AP')).

fcs :-
  retract(cyber(C)),
  assert(cyber(C)),
  (C == yes -> true ; fail),
  askq('security'),
  assert(recommend('FCS')).

ac :-
  retract(cyber(C)),
  assert(cyber(C)),
  (C == yes -> true ; fail),
  askq('security'),
  assert(recommend('AC')).

mb :-
  retract(biz(B)),
  assert(biz(B)),
  (B == yes -> true ; fail),
  askq('business'),
  assert(recommend('MB')).

ff :-
  retract(biz(B)),
  assert(biz(B)),
  (B == yes -> true ; fail),
  askq('business'),
  assert(recommend('FF')).