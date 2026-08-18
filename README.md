# SyndProxy private pool

## Current pool

- Alive now: 939
- Gold now: 334
- HTTP: 293 alive / 44 gold
- HTTPS: 199 alive / 9 gold
- SOCKS4: 220 alive / 141 gold
- SOCKS5: 227 alive / 140 gold

## Historical pool

- Discovered: 107059
- Ever alive: 14627
- Ever gold: 466

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
