# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 391
- HTTP: 94 alive / 60 gold
- HTTPS: 41 alive / 16 gold
- SOCKS4: 178 alive / 156 gold
- SOCKS5: 179 alive / 159 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48149
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
