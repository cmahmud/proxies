# SyndProxy private pool

## Current pool

- Alive now: 757
- Gold now: 383
- HTTP: 226 alive / 74 gold
- HTTPS: 102 alive / 15 gold
- SOCKS4: 229 alive / 156 gold
- SOCKS5: 200 alive / 138 gold

## Historical pool

- Discovered: 145558
- Ever alive: 25469
- Ever gold: 1060

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
