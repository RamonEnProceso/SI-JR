# Clientes
---

## POST /clientes

### Request

```
{
  "nombre": "Empresa ABC",
  "telefono": "1122334455",
  "email": "contacto@abc.com",
  "direccion": "Av. Siempreviva 123",
  "tipo_cliente_id": 1
}
```

### Response 201

```
{
  "id": 1,
  "nombre": "Empresa ABC",
  "telefono": "1122334455",
  "email": "contacto@abc.com",
  "direccion": "Av. Siempreviva 123",
  "tipo_cliente_id": 1
}
```

### Errores

#### Sin nombre
```
{
  "detail": "El nombre es obligatorio"
}
```
#### Sin teléfono
```
{
  "detail": "El teléfono es obligatorio"
}
```

#### Email ya en uso
```
{
  "detail": "Email ya en uso por otro cliente"
}
```

---

## GET /clientes

### Response 200

```
[
  {
  "id": 1,
  "nombre": "Empresa ABC",
  "telefono": "1122334455",
  "email": "contacto@abc.com",
  "direccion": "Av. Siempreviva 123",
  "tipo_cliente_id": 1
  },
  {
  "id": 2,
  "nombre": "Empresa DEF",
  "telefono": "6677889900",
  "email": "contacto@def.com",
  "direccion": "Av. Siempreviva 123",
  "tipo_cliente_id": 2
  },
  ...
]
```

#### Tipo de Cliente no encontrado
```
{
  "detail": "Tipo de cliente no encontrado"
}
```

---

## GET /clientes/{id}

### Response 200

```
{
  "id": 1,
  "nombre": "Empresa ABC",
  "telefono": "1122334455",
  "email": "contacto@abc.com",
  "direccion": "Av. Siempreviva 123",
  "tipo_cliente_id": 1
}
```

### Errores

#### Cliente no encontrado
```
{
  "detail": "Cliente no encontrado"
}
```

---

## PUT /clientes/{id}

### Request

```
{
  "nombre": "Empresa ABC",
  "telefono": "999999999",
  "email": "nuevo@email.com",
  "direccion": "Nueva dirección",
  "tipo_cliente_id": 1
}
```

### Response 200

```
{
  "detail": "Modificado correctamente"
}
```

### Errores

#### Cliente no encontrado
```
{
  "detail": "Cliente no encontrado"
}
```

---

## DELETE /clientes/{id}

### Errores

#### Cliente no encontrado
```
{
  "detail": "Cliente no encontrado"
}
```