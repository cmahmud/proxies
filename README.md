# SyndProxy private pool

## Current pool

- Alive now: 987
- Gold now: 379
- HTTP: 343 alive / 75 gold
- HTTPS: 187 alive / 18 gold
- SOCKS4: 210 alive / 125 gold
- SOCKS5: 247 alive / 161 gold

## Historical pool

- Discovered: 110856
- Ever alive: 15795
- Ever gold: 505

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
