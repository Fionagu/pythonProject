from pytest import mark


@mark.test_1
@mark.parametrize('tv_brand_1',['Sony', 'Sumsong'])
def test_parametized_1(tv_brand_1):
    print(f'{tv_brand_1} turns on')


@mark.test_2
def test_parametized_1(tv_brand_2):
    print(f'{tv_brand_2} turns on')



@mark.test_3
def test_parametized_1(tv_brand_3):
    print(f'{tv_brand_3} turns on')