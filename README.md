# SyndProxy private pool

## Current pool

- Alive now: 751
- Gold now: 388
- HTTP: 198 alive / 79 gold
- HTTPS: 156 alive / 21 gold
- SOCKS4: 208 alive / 146 gold
- SOCKS5: 189 alive / 142 gold

## Historical pool

- Discovered: 149513
- Ever alive: 26922
- Ever gold: 1089

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
