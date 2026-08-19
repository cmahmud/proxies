# SyndProxy private pool

## Current pool

- Alive now: 1026
- Gold now: 532
- HTTP: 350 alive / 159 gold
- HTTPS: 248 alive / 88 gold
- SOCKS4: 224 alive / 156 gold
- SOCKS5: 204 alive / 129 gold

## Historical pool

- Discovered: 119814
- Ever alive: 18079
- Ever gold: 714

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
