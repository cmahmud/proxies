# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 372
- HTTP: 81 alive / 45 gold
- HTTPS: 43 alive / 10 gold
- SOCKS4: 177 alive / 156 gold
- SOCKS5: 188 alive / 161 gold

## Historical pool

- Discovered: 172318
- Ever alive: 32974
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
