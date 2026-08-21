import magic_calc.basic_ops as myops
import magic_calc.advanced_ops
# result = magic_calc.basic_ops.add(10, 5)
result = myops.add(10, 5)

result1 = magic_calc.advanced_ops.sqrt(16)

result2 = magic_calc.advanced_ops.power(2, 6)

result3 = magic_calc.advanced_ops.magic_multiply(6)

print(f"10+5={result1} 10의 제곱근은 {result1}입니다. 16의 제곱근은 {result1}입니다. 2의 6제곱은 {result2}입니다. 6에 7을 곱하면 {result3}입니다.")

# import를 맨위에 모아서 써준다. 패키지를 모아주는 영역이다.
# 주석을 사용하고 import는 필요한 것만 위에 써주고 깔끔하게 코드 관리를 하기!