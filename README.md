# SyndProxy private pool

## Current pool

- Alive now: 904
- Gold now: 237
- HTTP: 288 alive / 33 gold
- HTTPS: 156 alive / 9 gold
- SOCKS4: 242 alive / 114 gold
- SOCKS5: 218 alive / 81 gold

## Historical pool

- Discovered: 86746
- Ever alive: 7591
- Ever gold: 337

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
