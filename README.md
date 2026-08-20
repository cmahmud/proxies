# SyndProxy private pool

## Current pool

- Alive now: 1426
- Gold now: 600
- HTTP: 573 alive / 195 gold
- HTTPS: 377 alive / 98 gold
- SOCKS4: 216 alive / 140 gold
- SOCKS5: 260 alive / 167 gold

## Historical pool

- Discovered: 138843
- Ever alive: 23110
- Ever gold: 914

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
