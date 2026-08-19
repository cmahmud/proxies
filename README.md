# SyndProxy private pool

## Current pool

- Alive now: 1029
- Gold now: 405
- HTTP: 282 alive / 76 gold
- HTTPS: 203 alive / 13 gold
- SOCKS4: 273 alive / 154 gold
- SOCKS5: 271 alive / 162 gold

## Historical pool

- Discovered: 131115
- Ever alive: 20576
- Ever gold: 868

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
