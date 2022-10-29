% sort in ascending order without deleting duplicates
mysort(List, Result) :- sort(0, @=<, List, Result).

% join two lists
join(List, X, Result) :- append(List, X, Result).