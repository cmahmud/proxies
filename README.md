# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 194
- HTTP: 153 alive / 41 gold
- HTTPS: 39 alive / 8 gold
- SOCKS4: 141 alive / 64 gold
- SOCKS5: 156 alive / 81 gold

## Historical pool

- Discovered: 170278
- Ever alive: 32721
- Ever gold: 1207

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
