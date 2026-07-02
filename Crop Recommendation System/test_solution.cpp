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
    
    cout << "Testing String Partitioning Solution\n";
    cout << "====================================\n\n";
    
    // Test cases with expected results
    vector<tuple<int, long long, int, string, long long>> tests = {
        {4, 12, 9, "1234", 2},
        {5, 100, 9, "12345", 8},
        {3, 10, 9, "123", 2},
        {2, 5, 9, "12", 1},
        {1, 9, 9, "5", 1},
        {3, 5, 9, "123", 1},
        {4, 10, 9, "1000", 1},
        {5, 50, 9, "12345", 3},
        {2, 99, 9, "99", 1},
        {3, 1, 9, "123", 0},
        {4, 2, 9, "1234", 0},
        {5, 3, 9, "12345", 0},
        {3, 0, 9, "123", 0},
        {1, 0, 9, "5", 0},
        {1, 0, 9, "0", 1},
        {2, 10, 9, "00", 0},
        {3, 10, 9, "001", 0},
        {4, 10, 9, "0001", 0},
        {5, 10, 9, "00001", 0},
        {3, 10, 9, "100", 1},
        {4, 10, 9, "1000", 1},
        {5, 10, 9, "10000", 1},
        {3, 10, 9, "999", 0},
        {4, 10, 9, "9999", 0},
        {5, 10, 9, "99999", 0}
    };
    
    int passed = 0, total = tests.size();
    
    for (int i = 0; i < tests.size(); i++) {
        auto [N, C, K, S, expected] = tests[i];
        long long result = Count(N, C, K, S);
        
        cout << "Test " << (i+1) << ": N=" << N << ", C=" << C << ", K=" << K << ", S=\"" << S << "\"\n";
        cout << "Expected: " << expected << ", Got: " << result;
        
        if (result == expected) {
            cout << " ✓ PASSED\n";
            passed++;
        } else {
            cout << " ✗ FAILED\n";
        }
        cout << "\n";
    }
    
    cout << "====================================\n";
    cout << "Results: " << passed << "/" << total << " tests passed\n";
    
    if (passed == total) {
        cout << "All tests passed! ✓\n";
    } else {
        cout << "Some tests failed! ✗\n";
    }
    
    return 0;
}

