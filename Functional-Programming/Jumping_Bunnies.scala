import java.io._;

object Solution {
    def main(args: Array[String]) {
        var N: Int = readLine().toInt;
        var J: Array[Int] = readLine().split(" ").map((x) => x.toInt);
        var point: Long = 1;
        
        for(j <- J) {
            point = lcm(point, j);
        }
        
        print(point);
    }


    def lcm(a: Long, b: Long): Long = {
        return a * (b / gcd(a, b));
    }

    def gcd(v1: Long, v2: Long): Long = {
        var a: Long = v1;
        var b: Long = v2;
        
        while (b != 0) {
            var c: Long = a % b;
            a = b;
            b = c;
        }
        
        return a;
    }
}
