# SyndProxy private pool

## Current pool

- Alive now: 858
- Gold now: 382
- HTTP: 217 alive / 79 gold
- HTTPS: 219 alive / 16 gold
- SOCKS4: 212 alive / 149 gold
- SOCKS5: 210 alive / 138 gold

## Historical pool

- Discovered: 149510
- Ever alive: 26869
- Ever gold: 1088

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
