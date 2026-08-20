# SyndProxy private pool

## Current pool

- Alive now: 701
- Gold now: 365
- HTTP: 166 alive / 70 gold
- HTTPS: 138 alive / 19 gold
- SOCKS4: 178 alive / 118 gold
- SOCKS5: 219 alive / 158 gold

## Historical pool

- Discovered: 148330
- Ever alive: 26044
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
