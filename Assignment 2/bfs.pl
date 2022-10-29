% helper predicate
prepend(L, X, [X | L]).

% if goal is at the head of the queue, return it
bfs([[Goal | Rest] | _], _, Goal, [Goal | Rest]).

% main recursive predicate: bfs(+Succ, +Queue, +Visited, +Goal, -Solution)
bfs([[State | Path] | Queue], Visited, Goal, Solution) :-
    findall(X, s(State, X), Next),    % find all neighboring states
    subtract(Next, Visited, Next1),            % remove already-visited states
    maplist(prepend([State | Path]), Next1, Next2), % prepend each state to path
    append(Queue, Next2, Queue2),              % add all new states to queue
    append(Next1, Visited, Visited1),          % add all new states to visited set
    bfs(Queue2, Visited1, Goal, Solution).   % recurse

% top-level predicate: bfs(+Succ, Start, +Goal, -Solution)
bfs(Start, Goal, Solution) :-
    bfs([[Start]], [Start], Goal, Solution1),
    reverse(Solution1, Solution).