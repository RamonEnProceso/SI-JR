# Pedidos del Cliente

## Funcionalidades principales
- Sistema de login con roles
- Gestión de clientes
- Creación y administración de órdenes de trabajo
- Asignación de técnicos a órdenes
- Checklist dinámico por tipo de trabajo
- Subida de imágenes desde dispositivos móviles
- Registro de observaciones por orden
- Historial completo por cliente
- Estados de orden de trabajo (pendiente, asignada, en curso, finalizada, observada)

## Roles del Sistema

<table align="center">
  <tr>
    <td align="center">
      👨‍💻 Administrador
    </td>
    <td align="center">
      👨‍🏭 Técnico
    </td>
  </tr>
  <tr>
    <td align="left">
        - Alta y gestión de clientes
        <br/>- Creación de órdenes de trabajo
        <br/>- Asignación de técnicos
        <br/>- Gestión de checklist de tareas
        <br/>- Visualización del estado general <br/>de todos los trabajos
        <br/>- Acceso al historial completo de clientes
    </td>
    <td align="left">
        - Acceso a órdenes asignadas
        <br/>- Ejecución de checklist
        <br/>- Carga de fotos
        <br/>- Gestión de checklist de tareas
        <br/>- Registro de observaciones
        <br/>- Cambio de estado de la orden
    </td>
  </tr>
</table>

## Gestión
### Cliente
> Datos que tiene un cliente

<table align="center">
  <tr>
    <td align="center">
      👤 Cliente
    </td>
  </tr>
  <tr>
    <td align="left">
        - Nombre o razón social
        <br/>- Teléfono
        <br/>- Email
        <br/>- Dirección
        <br/>- Tipo de cliente
        <br/>- Contacto responsable
        <br/>- Observaciones
    </td>
  </tr>
</table>

### Órdenes
> Datos que tiene cada órden

<table align="center">
  <tr>
    <td align="center">
      📄 Órden de Trabajo
    </td>
  </tr>
  <tr>
    <td align="left">
        - Número automático.
    <br/>- Cliente asociado
    <br/>- Dirección del servicio
    <br/>- Fecha programada
    <br/>- Horario estimado
    <br/>- Técnico asignado
    <br/>- Rubro
    <br/>- Descripción
    <br/>- Prioridad
    <br/>- Estado
    <br/>- Observaciones internas
    </td>
  </tr>
</table>

Cada órden cuenta con checklist y fotos propias.

## Historial
> Qué datos el sistema conserva

<table align="center">
  <tr>
    <td align="center">
      🕐 Historial
    </td>
  </tr>
  <tr>
    <td align="left">
        - Fecha
    <br/>- Técnico
    <br/>- Descripción
    <br/>- Checklist completado
    <br/>- Fotografías
    <br/>- Observaciones
    <br/>- Recomendaciones
    <br/>- Estado final
  </tr>
</table>

## Dashboard
> Qué datos el administrador visualiza

<table align="center">
  <tr>
    <td align="center">
      📠 Dashboard
    </td>
  </tr>
  <tr>
    <td align="left">
        - Órdenes pendientes
    <br/>- Órdenes de hoy
    <br/>- Órdenes asignadas
    <br/>- Trabajos en curso
    <br/>- Trabajos finalizados
    <br/>- Técnicos activos
    <br/>- Clientes recientes
  </tr>
</table>