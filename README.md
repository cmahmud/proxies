# SyndProxy validated proxy pool

## Current pool

- Alive now: 471
- Gold now: 382
- HTTP: 94 alive / 66 gold
- HTTPS: 33 alive / 14 gold
- SOCKS4: 176 alive / 152 gold
- SOCKS5: 168 alive / 150 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48168
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
