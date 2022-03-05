# Pomodoro

---
Pomodoro timer web app feito com Python e Django, seguindo a live coding do
[Gilson Filho](https://www.youtube.com/channel/UCHDOicoGqIKPg1b9lr-OkxA/videos).

# Simple API Doc

---

## Tarefas

---

### Lista de tarefas cadastradas

**GET** /api/tasks/

```json
[
  {
    "uid": "5819ef1f-22dc-4276-a389-57cb9770eb7d",
    "description": "Tarefa 01",
    "created_at": "2022-05-03T15:23:00"
  },
  {
    "uid": "ef4a14db-e8f2-4964-a36b-765324660cea",
    "description": "Tarefa 02",
    "created_at": "2022-05-03T15:25:00"
  }
]
```

### Lista uma tarefa por UID

**GET** /api/tasks/{uid}/

```json
{
  "uid": "ef4a14db-e8f2-4964-a36b-765324660cea",
  "description": "Tarefa 02",
  "created_at": "2022-05-03T15:25:00"
}
```

### Cria uma nova tarefa

**POST** /api/tasks/

```json
{
  "description": "Nova tarefa"
}
```

### Atualiza uma tarefa por UID

**PUT** /api/tasks/{uid}/

```json
{
  "description": "Atualiza tarefa"
}
```

### Remove uma tarefa por UID

**DELETE** /api/tasks/{uid}/

```json
[
  {
    "uid": "ef4a14db-e8f2-4964-a36b-765324660cea",
    "description": "Tarefa 02",
    "created_at": "2022-05-03T15:25:00",
    "deleted_at": "2022-05-03T15:28:00"
  }
]
```

## Pomodoros

---

### Listas os pomodoros de uma tarefa

**GET** api/tasks/{uid}/pomodoro/

```json
{
  "uid": "29cabb7e-bfb7-4080-a185-e5f4a7beb2c5",
  "description": "Tarefa",
  "total_pomodoros": 3,
  "total_interruptions": 0,
  "pomodoros": [
    {
      "started_at": "2022-05-03T15:40:00",
      "ended_at": "2022-05-03T16:05:00",
      "completed": true,
      "interrupted": false
    },
    {
      "started_at": "2022-05-03T16:10:00",
      "ended_at": "2022-05-03T16:35:00",
      "completed": true,
      "interrupted": false
    },
    {
      "started_at": "2022-05-03T16:40:00",
      "ended_at": "2022-05-03T17:05:00",
      "completed": true,
      "interrupted": false
    }
  ]
}
```

### Adiciona um pomodoro a uma tarefa

**POST** api/tasks/{uid}/pomodoro/

```json
{
  "started_at": "",
  "ended_at": "",
  "completed": true,
  "interrupted": false
}
```