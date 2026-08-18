# SyndProxy private pool

## Current pool

- Alive now: 913
- Gold now: 333
- HTTP: 295 alive / 43 gold
- HTTPS: 165 alive / 9 gold
- SOCKS4: 222 alive / 141 gold
- SOCKS5: 231 alive / 140 gold

## Historical pool

- Discovered: 107059
- Ever alive: 14591
- Ever gold: 466

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
