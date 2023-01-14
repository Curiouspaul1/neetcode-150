function minWindow(s: string, t: string): string {
    if (t.length > s.length) {
        return "";
    }

    let tMap: { [key: string]: number } = {};
    for (let i = 0; i < t.length; i++) {
        tMap[t[i]] = (tMap[t[i]] || 0) + 1;
    }

    let minStart = 0;
    let minEnd = s.length;
    let minLength = s.length + 1;

    let windowMap: { [key: string]: number } = {};
    let count = 0;
    let start = 0;
    let end = 0; 

    while (end < s.length) {
        if (tMap[s[end]] !== undefined) {
            windowMap[s[end]] = (windowMap[s[end]] || 0) + 1;
            if (windowMap[s[end]] <= tMap[s[end]]) {
                count++;
            }
        }
        if (count === t.length) {
            while (tMap[s[start]] === undefined || windowMap[s[start]] > tMap[s[start]]) {
                if (tMap[s[start]] !== undefined) {
                    windowMap[s[start]]--;
                }
                start++;
            }

            if (end - start + 1 < minLength) {
                minStart = start;
                minEnd = end;
                minLength = end - start + 1;
            }
        }
        end++;
    }

    if (minLength === s.length + 1) {
        return "";
    } else {
        return s.substring(minStart, minEnd + 1);
    }
}
