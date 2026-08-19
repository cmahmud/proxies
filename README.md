# SyndProxy private pool

## Current pool

- Alive now: 1025
- Gold now: 547
- HTTP: 351 alive / 156 gold
- HTTPS: 260 alive / 106 gold
- SOCKS4: 212 alive / 150 gold
- SOCKS5: 202 alive / 135 gold

## Historical pool

- Discovered: 127371
- Ever alive: 19907
- Ever gold: 804

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
