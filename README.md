# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 416
- HTTP: 95 alive / 63 gold
- HTTPS: 45 alive / 22 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 176 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47085
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
