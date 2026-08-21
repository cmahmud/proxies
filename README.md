# SyndProxy private pool

## Current pool

- Alive now: 1047
- Gold now: 406
- HTTP: 357 alive / 105 gold
- HTTPS: 273 alive / 28 gold
- SOCKS4: 205 alive / 148 gold
- SOCKS5: 212 alive / 125 gold

## Historical pool

- Discovered: 153184
- Ever alive: 28464
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
