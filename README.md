# SyndProxy private pool

## Current pool

- Alive now: 1103
- Gold now: 326
- HTTP: 407 alive / 38 gold
- HTTPS: 227 alive / 10 gold
- SOCKS4: 237 alive / 148 gold
- SOCKS5: 232 alive / 130 gold

## Historical pool

- Discovered: 106888
- Ever alive: 14137
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
