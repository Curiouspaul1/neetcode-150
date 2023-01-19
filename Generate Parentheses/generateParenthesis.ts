function generateParenthesis(n: number): string[] {
    const result: string[] = [];
    const dfs = (s: string, left: number, right: number) => {
        if (left === n && right === n) {
            result.push(s);
            return;
        }
        if (left < n) {
            dfs(s + '(', left + 1, right);
        }
        if (right < left) {
            dfs(s + ')', left, right + 1);
        }
    }
    dfs('', 0, 0);
    return result;
}