# SyndProxy private pool

## Current pool

- Alive now: 1023
- Gold now: 408
- HTTP: 345 alive / 78 gold
- HTTPS: 215 alive / 27 gold
- SOCKS4: 217 alive / 147 gold
- SOCKS5: 246 alive / 156 gold

## Historical pool

- Discovered: 156437
- Ever alive: 29558
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
