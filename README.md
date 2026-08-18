# SyndProxy private pool

## Current pool

- Alive now: 1342
- Gold now: 235
- HTTP: 621 alive / 35 gold
- HTTPS: 249 alive / 9 gold
- SOCKS4: 239 alive / 111 gold
- SOCKS5: 233 alive / 80 gold

## Historical pool

- Discovered: 86746
- Ever alive: 7591
- Ever gold: 336

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
