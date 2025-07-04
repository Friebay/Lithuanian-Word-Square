import java.io.BufferedReader;
import java.io.FileReader;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.*;

public class App
{
    static final String ALPHABET      = "abcdefghijklmnopqrstuvyząčęėįšųūž";
    static final int    ALPHABET_SIZE = ALPHABET.length();

    public static void main(String[] args) {
        final int n = 11; // word square size

        System.out.println("start: " + now());

        final int[][] t = loadDictionary("C:\\Users\\zabit\\Documents\\GitHub\\Lithuanian-Word-Square\\11_length_words.txt", n); // trie of dictionary words of length n

        final boolean[][][] ts = trieSet(t, n);

        final int[] si = traversal(n, true); 
        final int[] sj = traversal(n, false); 
        final int nSteps = si.length;

        final int [][] m = new int[n][n]; 
        final int [][] h = new int[n][n];  
        final int [][] v = new int[n][n]; 

        final boolean [][][] c = new boolean[n][n][ALPHABET_SIZE];

        final Character startCharacter = 'a';
        int step = 0;
        boolean forward = false;
        m[0][0] = ALPHABET.indexOf(startCharacter) - 1;

        long iteration = 0;
        int maxStep = 0;
        int nSolutions = 0;

        for(;;) {
            final int i = si[step];
            final int j = sj[step];
            final int[] hL = j == 0 ? t[0] : t[h[i][j - 1]];
            final int[] vL = i == 0 ? t[0] : t[v[i - 1][j]];
            final int[] hU = i == 0 ? t[0] : t[h[j][i - 1]];
            final int[] vU = j == 0 ? t[0] : t[v[j - 1][i]];
            int match = forward ? 0 : m[i][j] + 1;
            for (; match < ALPHABET_SIZE; ++match) {
                 if (hL[match] == 0 || vL[match] == 0 || hU[match] == 0 || vU[match] == 0)
                    continue;
                if (j > 0) {
                    final boolean[][] vNode = ts[vL[match]];
                    boolean isMatch = true;
                    final int nRows = i + j >= n ? n - i : j;
                    for (int d = nRows; d > 0; --d) {
                        if (i + d >= n)
                            break;
                        final boolean[] s1 = vNode[d];
                        final int hNode = h[i + d][j - d];
                        final boolean[] s2 = ts[hNode][d];
                        boolean isSetMatch = false;
                        for (int k = 0; k < ALPHABET_SIZE; ++k) {
                            if (s1[k] && s2[k]) {
                                isSetMatch = true;
                                break;
                            }
                        }
                        if (!isSetMatch) {
                            isMatch = false;
                            break;
                        }
                    }
                    if (!isMatch)
                        continue;
                }
                if (i > j) {
                    final boolean[][] vNode = ts[vU[match]];
                    boolean isMatch = true;
                    final int nr = i - j;
                    for (int d = 1; d < nr; ++d) {

                        final boolean[] s1 = vNode[d];
                        final int hNode = h[j + d][i - d - 1];
                        final boolean[] s2 = ts[hNode][d + 1];

                        boolean isSetMatch = false;
                        for (int k = 0; k < ALPHABET_SIZE; ++k) {
                            if (s1[k] && s2[k]) {
                                isSetMatch = true;
                                break;
                            }
                        }

                        if (!isSetMatch) {
                            isMatch = false;
                            break;
                        }
                    }

                    if (!isMatch)
                        continue;
                }

                break;
            }


            if (match < ALPHABET_SIZE) {
                m[i][j] = match;
                m[j][i] = match;

                h[i][j] = hL[match];
                v[i][j] = vL[match];

                h[j][i] = hU[match];
                v[j][i] = vU[match];

                if (++step == nSteps) {
                    ++nSolutions;
                    System.out.printf("\nSolution %d found: loop count %,d  %s  \n\n", nSolutions, iteration, now());
                    display(m, i, j, si, sj, step);
                    --step;
                    forward = false;
                    continue;
                }

                if (step > maxStep && nSolutions == 0) {
                    System.out.printf("\n\n\nTemp solution after %,d iterations  STEP = %d/%d  %s\n\n",
                                        iteration, step, nSteps, now());
                    display(m, i, j, si, sj, step);
                    maxStep = step;
                }

                forward = true;
            } else {
                if (--step < 0)
                    break;

                if (step == 0)
                    System.out.printf("passed the first character %s    Number of iterations %,d    %s\n",
                                       ALPHABET.charAt(m[0][0]), iteration, now());
                forward = false;
            }

            ++iteration;
        }

        System.out.printf("\n\nNumber of solutions found: %d\ntotal loop count %,d\nfinish time  %s  \n\n",
                     nSolutions, iteration, now());
    }

    private static void display(int[][] m, int x, int y, int[] si, int[] sj, final int nStep) {
        final int n = m.length;

        boolean[][] o = new boolean[n][n];
        for (int step = 0; step < nStep; ++step) {
            o[si[step]][sj[step]] = true;
            o[sj[step]][si[step]] = true;
        }

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                System.out.print(o[i][j] ? ALPHABET.charAt(m[i][j]) : '.');
            }
            System.out.println();
        }
        System.out.println("\n\n");
    }

    private static String now() {
        return LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
    }

    private static int[][] loadDictionary(final String fileName, final int n) {

        final List<String> words = loadDictionaryWords(fileName, n);
        if (words.size() < n)
            throw new RuntimeException("at least " + n + " words words of length " + n + " needed in dictionary " + fileName);

        final List<Integer> zeros = Collections.nCopies(ALPHABET_SIZE, 0);
        final ArrayList<ArrayList<Integer>> trie = new ArrayList<>();
        trie.add(new ArrayList<>(zeros)); 

        for (final String word : words) {
            int node = 0;

            for (final char c : word.toCharArray()) {
               
                final int index = ALPHABET.indexOf(c);
                if (trie.get(node).get(index) == 0) {
                    trie.get(node).set(index, trie.size()); 
                    trie.add(new ArrayList<>(zeros)); 
                }

                node = trie.get(node).get(index);
            }
        }

        int[][] result = new int[trie.size()][ALPHABET_SIZE];

        for (int i = 0, size = trie.size(); i < size; ++i) {
            for (int j = 0; j < ALPHABET_SIZE; ++j) {
                result[i][j] = trie.get(i).get(j);
            }
        }

        System.out.printf("%,d words of length %d loaded\n", words.size(), n);

        return result;
    }

    private static List<String> loadDictionaryWords(final String fileName, final int n) {
        final Set<String> set = new HashSet<>();

        try (BufferedReader br = new BufferedReader(new java.io.InputStreamReader(
                new java.io.FileInputStream(fileName), java.nio.charset.StandardCharsets.UTF_8))) {
            String word;
            while ((word = br.readLine()) != null) {
                if (word.length() != n ||
                        Character.isDigit(word.charAt(0)) ||
                        Character.isUpperCase(word.charAt(0)) ||
                        ! isValidWord(word))
                    continue;

                set.add(word);
            }
        }
        catch (Exception e) {
            throw new RuntimeException(e);
        }

        final List<String> list = new ArrayList<>(set);
        Collections.sort(list);
        return list;
    }

    private static boolean[][][] trieSet(final int[][] trie, final int n) {
        final boolean[][][] result = new boolean[trie.length][n + 1][ALPHABET_SIZE];

        for (int i = 0, size = trie.length; i < size; ++i)
            for (int d = 0; d < n; ++d)
                for (final int charCode : trieSet(trie, i, d)) {
                    result [i][d + 1][charCode] = true;
                }

        return result;
    }

    private static Set<Integer> trieSet(final int[][] trie, final int node, final int distance) {
        final Set<Integer> result = new HashSet<>();
        final int[] subNodes = trie[node];

        for (int i = 0, size = subNodes.length; i < size; ++i) {
            final int nextNode = subNodes[i];
            if (nextNode == 0)
                continue;

            if (distance == 0)
                result.add(i);
            else
                result.addAll(trieSet(trie, nextNode, distance - 1));
        }

        return result;
    }

    private static int[] traversal(final int n, final boolean isIcoordinate) {
        final int[] result = new int[n * (n + 1) / 2];
        int idx = 0;

        for (int k = 0 ; k < n * 2 ; ++k) {
            for (int j = 0 ; j <= k ; ++j) {
                final int i = k - j;
                if (i < n && j <= i ) {
                    result[idx++] = isIcoordinate ? i : j;
                }
            }
        }

        return result;
    }

static boolean isValidWord(final String word) {
    for (final char c : word.toCharArray()) {
        if (ALPHABET.indexOf(c) == -1)
            return false;
    }
    return true;
    }
}