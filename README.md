# SyndProxy private pool

## Current pool

- Alive now: 641
- Gold now: 388
- HTTP: 166 alive / 70 gold
- HTTPS: 98 alive / 19 gold
- SOCKS4: 182 alive / 145 gold
- SOCKS5: 195 alive / 154 gold

## Historical pool

- Discovered: 146602
- Ever alive: 25681
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
