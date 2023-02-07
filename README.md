# CSCI-3302-Data-Structure-Algorithms
Individual assignment for subject CSCI 3302 Sem 1 22/23

The Floyd-Warshall algorithm is a general-purpose algorithm for finding the shortest paths in a weighted graph. It was modified for the specific task of finding a portfolio with the maximum Sharpe ratio in the field of risk arbitrage.

In risk arbitrage, the goal is to find a portfolio of stocks that has the highest ratio of expected return to risk. The Sharpe ratio is a common measure of risk-adjusted return, and it is calculated as the difference between the expected return and the risk-free return (such as the return on a US Treasury bond), divided by the volatility or risk of the portfolio.

The Floyd-Warshall algorithm was modified to calculate the Sharpe ratio of each pair of stocks and choose the pair with the highest Sharpe ratio as the portfolio. This is done by iterating over all pairs of stocks, calculating the Sharpe ratio of a portfolio consisting of those two stocks, and updating the weight of the portfolio if it has a higher Sharpe ratio.

The Floyd-Warshall algorithm was chosen for this task because it is a well-known algorithm for finding the shortest paths in a graph. It is relatively simple to modify for this specific application.

To modify the Floyd-Warshall algorithm for risk arbitrage, we will need to define a new function that takes in a distance matrix (d) representing the expected returns of each pair of stocks and a risk matrix (r) representing the volatility or risk of each pair of stocks. The function should return the Sharpe matrix (sharpe) that can be used to build a portfolio with the highest Sharpe ratio. The Sharpe Ratio is a measure of risk-adjusted return, which compares the return of an investment to its volatility.

The risk_arbitrage function takes two inputs:
d is a 2D array that represents the returns of the investments.
r is a 2D array that represents the risk of the investments.

It starts by creating a 2D array of size n x n with all elements initialized to zero. Then it populates the Sharpe matrix with the ratio of return to volatility by using the following formula : (d[i] - r) / (d[j] - r) where i and j are the nodes of the graph.

After that, it applies the Floyd-Warshall algorithm to find the path with the highest Sharpe Ratio between any two nodes in the graph. The min operator is used here to select the path with the highest Sharpe Ratio. Finally, it returns the Sharpe matrix where sharpe[i][j] represents the Sharpe Ratio of the path between node i and node j. To use the code, change any value in the d or r matrix to get the desired Sharpe Ratio.
