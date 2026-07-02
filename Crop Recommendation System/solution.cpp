#include <bits/stdc++.h>

using namespace std;

long long Count(int N, long long C, int K, const string& S) {
    // Calculate modulo value
    long long MOD = 1;
    for (int i = 0; i < K; i++) {
        MOD *= 10;
    }
    
    // Special case: if C is 0, only single digit 0 is allowed
    if (C == 0) {
        if (N == 1 && S[0] == '0') return 1;
        return 0;
    }
    
    // dp[i] represents the number of valid ways to partition string from index i to end
    vector<long long> dp(N + 1, 0);
    dp[N] = 1; // Base case: empty string has 1 way to partition
    
    for (int i = N - 1; i >= 0; i--) {
        // Try all possible lengths starting from position i
        long long current_num = 0;
        
        for (int len = 1; len <= N - i; len++) {
            // Check for leading zeros
            if (len > 1 && S[i] == '0') {
                break; // Leading zero not allowed for multi-digit numbers
            }
            
            // Build the number digit by digit, check for overflow
            if (current_num > C / 10) {
                break; // Will overflow on next multiplication
            }
            current_num = current_num * 10 + (S[i + len - 1] - '0');
            
            // Check if current number exceeds C
            if (current_num > C) {
                break; // No need to check longer numbers
            }
            
            // Add the ways from the remaining string
            dp[i] = (dp[i] + dp[i + len]) % MOD;
        }
    }
    
    return dp[0];
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, K;
    long long C;
    string S;
    
    // Read N, C, K from first line
    cin >> N >> C >> K;
    
    // Read string S from second line
    cin >> S;
    
    long long out_ = Count(N, C, K, S);
    cout << out_ << endl;
    
    return 0;
}
