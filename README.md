# SyndProxy private pool

## Current pool

- Alive now: 1068
- Gold now: 484
- HTTP: 366 alive / 127 gold
- HTTPS: 264 alive / 78 gold
- SOCKS4: 202 alive / 124 gold
- SOCKS5: 236 alive / 155 gold

## Historical pool

- Discovered: 119691
- Ever alive: 17864
- Ever gold: 693

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
