best_first([[Goal|Path]|_],Goal,[Goal|Path],0).
best_first([Path|Queue],Goal,FinalPath,N) :-
  extend(Path,NewPaths), 
  append(Queue,NewPaths,Queue1),
  sort_queue1(Queue1,NewQueue), wrq(NewQueue),
  best_first(NewQueue,Goal,FinalPath,M),
  N is M+1.

extend([Node|Path],NewPaths) :-
  findall([NewNode,Node|Path],
    (arc(Node,NewNode,_), 
    \+ member(NewNode,Path)), % for avoiding loops
    NewPaths).