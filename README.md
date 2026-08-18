# SyndProxy private pool

## Current pool

- Alive now: 878
- Gold now: 241
- HTTP: 270 alive / 29 gold
- HTTPS: 124 alive / 9 gold
- SOCKS4: 252 alive / 115 gold
- SOCKS5: 232 alive / 88 gold

## Historical pool

- Discovered: 86712
- Ever alive: 6880
- Ever gold: 322

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
