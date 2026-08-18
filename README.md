# SyndProxy private pool

## Current pool

- Alive now: 940
- Gold now: 333
- HTTP: 294 alive / 44 gold
- HTTPS: 197 alive / 9 gold
- SOCKS4: 218 alive / 142 gold
- SOCKS5: 231 alive / 138 gold

## Historical pool

- Discovered: 107059
- Ever alive: 14575
- Ever gold: 465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
