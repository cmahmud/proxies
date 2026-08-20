# SyndProxy private pool

## Current pool

- Alive now: 741
- Gold now: 366
- HTTP: 180 alive / 71 gold
- HTTPS: 145 alive / 18 gold
- SOCKS4: 189 alive / 119 gold
- SOCKS5: 227 alive / 158 gold

## Historical pool

- Discovered: 148330
- Ever alive: 26048
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
