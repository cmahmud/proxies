# SyndProxy private pool

## Current pool

- Alive now: 653
- Gold now: 351
- HTTP: 173 alive / 69 gold
- HTTPS: 112 alive / 20 gold
- SOCKS4: 172 alive / 124 gold
- SOCKS5: 196 alive / 138 gold

## Historical pool

- Discovered: 145577
- Ever alive: 25576
- Ever gold: 1066

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
