# SyndProxy private pool

## Current pool

- Alive now: 1148
- Gold now: 379
- HTTP: 361 alive / 75 gold
- HTTPS: 312 alive / 18 gold
- SOCKS4: 225 alive / 125 gold
- SOCKS5: 250 alive / 161 gold

## Historical pool

- Discovered: 110856
- Ever alive: 15894
- Ever gold: 505

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
