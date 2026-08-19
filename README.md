# SyndProxy private pool

## Current pool

- Alive now: 1035
- Gold now: 393
- HTTP: 333 alive / 69 gold
- HTTPS: 235 alive / 15 gold
- SOCKS4: 244 alive / 153 gold
- SOCKS5: 223 alive / 156 gold

## Historical pool

- Discovered: 129331
- Ever alive: 20494
- Ever gold: 865

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
