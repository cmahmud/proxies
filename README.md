# SyndProxy private pool

## Current pool

- Alive now: 972
- Gold now: 359
- HTTP: 308 alive / 70 gold
- HTTPS: 222 alive / 13 gold
- SOCKS4: 215 alive / 128 gold
- SOCKS5: 227 alive / 148 gold

## Historical pool

- Discovered: 129290
- Ever alive: 20326
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
