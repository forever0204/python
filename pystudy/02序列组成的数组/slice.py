# 切片
# substring
s = 'bicycle'
print(s[::3])
print(s[0:s.__len__():3])
# s[a:b:c] 的形式对 s 在 a 和 b 之间以 c 为间隔取值
invoice = """
... 0.....6................................40........52...55........
... 1909 Pimoroni PiBrella                   $17.50   3   $52.50
... 1489 6mm Tactile Switch x20               $4.95   2    $9.90
... 1510 Panavise Jr. - PV-201               $28.00   1   $28.00
... 1601 PiTFT Mini Kit 320x240              $34.95   1   $34.95
... """
SKU = slice(0, 6)
DESCRIPTION = slice(6,40)
UNIT_PRICE = slice(40,52)
ITEM_TOTAL = slice(55, None)
line_items = invoice.split('\n')[2:]
for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])