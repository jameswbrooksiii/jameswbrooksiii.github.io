%%%%%%%%%%%%%%%%%%%%%%%%
% James Brooks         %
% February 18th, 2022  %
% CSC 330-002          %
% Winter 2021-2022     %
% Assignment #: 7 (e3) %
%%%%%%%%%%%%%%%%%%%%%%%%

function y = e3(b,n)
% y will be the sum, i is the current number being raised to
y = 0;
i = 1;
% When we reach the specified n, the final sum has been reached.
while i <= n
    % Current square is specified b raised to current i
    s = b^i;
    % y is the sum (starts at zero) plus the current square
    y = y+s;
    % Increase i by 1
    i = i+1;
end
% y is automatically displayed as the function's ans at the end