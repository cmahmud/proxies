# SyndProxy private pool

## Current pool

- Alive now: 980
- Gold now: 345
- HTTP: 314 alive / 49 gold
- HTTPS: 196 alive / 13 gold
- SOCKS4: 235 alive / 142 gold
- SOCKS5: 235 alive / 141 gold

## Historical pool

- Discovered: 107067
- Ever alive: 14666
- Ever gold: 468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
