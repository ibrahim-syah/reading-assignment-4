clear; clc; close all;

data = csvread('1.01. Simple linear regression.csv',1 , 0);

% Define x and y
x = data(:,1);
y = data(:,2);

% Create a function to plot the data
function plotData(x,y)
plot(x,y,'rx','MarkerSize',8); % Plot the data
end

% Plot the data
plotData(x,y);
xlabel('SAT scores'); % Set the x-axis label
ylabel('GPAs'); % Set the y-axis label
fprintf('Program paused. Press enter to continue.\n');
pause;

% Count how many data points we have
m = length(x);
% Add a column of all ones (intercept term) to x
X = [ones(m, 1) x];

% Calculate theta
theta = (pinv(X'*X))*X'*y

% Plot the fitted equation we got from the regression
hold on; % this keeps our previous plot of the training data visible
plot(X(:,2), X*theta, '-')
legend('Training data', 'Linear regression')
hold off % Do not put any more plots on this figure