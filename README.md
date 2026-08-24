# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 381
- HTTP: 106 alive / 61 gold
- HTTPS: 39 alive / 9 gold
- SOCKS4: 168 alive / 155 gold
- SOCKS5: 176 alive / 156 gold

## Historical pool

- Discovered: 179062
- Ever alive: 33439
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
