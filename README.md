# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 401
- HTTP: 93 alive / 61 gold
- HTTPS: 36 alive / 17 gold
- SOCKS4: 174 alive / 158 gold
- SOCKS5: 186 alive / 165 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48253
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
