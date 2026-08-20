# SyndProxy private pool

## Current pool

- Alive now: 766
- Gold now: 379
- HTTP: 227 alive / 74 gold
- HTTPS: 114 alive / 15 gold
- SOCKS4: 222 alive / 152 gold
- SOCKS5: 203 alive / 138 gold

## Historical pool

- Discovered: 145552
- Ever alive: 25469
- Ever gold: 1060

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
