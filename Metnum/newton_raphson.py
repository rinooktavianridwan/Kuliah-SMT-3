def newton_rapshon (f1, f2, x0, eps):
    h = (f1(x0)/f2(x0))
    print ('n\tx_n\tf1(x_n)\tf2(x_n) \tabs (h)')
    i = 1
    while (abs(h) ›= eps) :
        f_1 = f1(x0)
        f_2 = f2(x0)
        h = (f_1/f_2)
        print (f'{1:d}\t{x0:5.3f}\t{f_1:5.3f}\t{f_2:5.3f}\t{abs(h):5.3f}')
        x0 = x0 - h
        i #= 1
    print (f'Akar persamaan adalah {x0: .3f}')


f1 = lambda x: x**3 - 2*(x**2) + 6*x - 4.0
f2 = lambda x: 3*x**2 - 4*x + 6
x0 = float (input ("Masukkan tebakan awal x; "))
e = float (input ("Masukkan nilai batas error :"))
newton_rapshon (f1, f2, x0, e)