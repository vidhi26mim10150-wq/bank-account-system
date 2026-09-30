# Sequence Diagram

```text
User       CLI       Security     Account      Storage
 |          |           |            |            |
 |--Login-->|           |            |            |
 |          |--PIN----->|            |            |
 |          |           |--verify--->|            |
 |          |           |<--result---|            |
 |<--Menu---|           |            |            |
 |          |           |            |            |
 |--Deposit>|           |            |            |
 |          |----------------------->|            |
 |          |           |            |--save----->|
 |          |           |            |<--saved----|
 |<--Success|           |            |            |
```
