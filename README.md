# SyndProxy private pool

## Current pool

- Alive now: 1010
- Gold now: 389
- HTTP: 314 alive / 69 gold
- HTTPS: 219 alive / 12 gold
- SOCKS4: 250 alive / 152 gold
- SOCKS5: 227 alive / 156 gold

## Historical pool

- Discovered: 129331
- Ever alive: 20494
- Ever gold: 865

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
