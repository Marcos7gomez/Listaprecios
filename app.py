from flask import Flask, render_template, request, url_for, redirect, send_file
import imgkit

from forms import ProductoForm, MyForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave_secreta'  # Reemplaza con tu clave secreta


# class MyForm(FlaskForm):
#     fecha_hora = DateTimeField('Fecha y Hora', default=datetime.now().strftime('%d-%m-%y %H:%M:%S'))


@app.route('/')
def home():
    return render_template('home.html')


# class Lista(self, tipo_producto, precio, fecha):
#     self.tipo_producto = tipo_producto
#     self.precio = precio
#     self


precios = []


@app.route('/agregar_producto', methods=['GET', 'POST'])
def agregar_producto():
    form = ProductoForm()
    fecha = MyForm()

    if form.validate_on_submit():
        tipo_producto = form.tipo_producto.data
        precio = form.precio.data
        fecha_actual = fecha.fecha_hora.data
        precios.append({'tipo_producto': tipo_producto, 'precio': precio, fecha_actual: 'fecha actual'})
        print(f'Nuevo elemento a la lista: {precios}')
        return redirect(url_for('agregar_producto'))
    return render_template('nueva_lista.html', form=form, fecha=fecha, precios=precios)


@app.route('/lista_precios')
def lista_precios():
    return render_template('lista_precios.html', precios=precios)


@app.route('/descargar_imagen', methods=['GET'])
def descargar_imagen():
    rendered = render_template('lista_precios.html')

    # Ruta temporal para guardar la imagen generada
    nombre_archivo = 'tabla.png'

    # Genera la imagen desde el HTML usando imgkit
    imgkit.from_string(rendered, nombre_archivo, options={'format': 'png'})

    # Envía el archivo para descargar
    return send_file(nombre_archivo, as_attachment=True)
