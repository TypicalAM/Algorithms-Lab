cd "/home/Adam/Notatki/Studia/Semestr 2/Algorytmy i struktury danych/lab/1 - Algorytmy sortowania/Sprawozdanie/second try/"
// Reading the fist csv
M = csvRead("out_2.0.csv")(:, [2:11]);
tests = M(1,:);
quickmid = M(2,:);
counting = M(3,:);
merge = M(4,:);
heap = M(5,:);
insertion = M(6,:);
selection = M(7,:);
bubble = M(8,:);

subplot(221)
plot(tests, bubble, insertion, selection, heap, merge, counting, quickmid)

M = csvRead("out_3.1.csv")(:, [2:11]);
tests = M(1,:);
quickmid = M(2,:);
quicktop = M(3,:);
insertion = M(4,:);

subplot(222)
plot(tests, insertion, quickmid, quicktop)

M = csvRead("out_3.1.csv")(:, [2:11]);
tests = M(1,:);
insertion = M(2,:);
quickmid = M(3,:);
quicktop = M(4,:);

subplot(223)
plot(tests, insertion, quickmid, quicktop)
