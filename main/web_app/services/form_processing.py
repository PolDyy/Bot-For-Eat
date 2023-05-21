from .cart import Cart


def add_product_form_processing(form):

    if form.validate_on_submit():
        product_data = form.get_dict()
        Cart().add_product(product_data)
        return {'status': 'success', 'message': "Добавлено к заказу!"}
    return {'status': 'error', 'message': "Ошибка формы"}
