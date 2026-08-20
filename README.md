# SyndProxy private pool

## Current pool

- Alive now: 1031
- Gold now: 383
- HTTP: 306 alive / 94 gold
- HTTPS: 263 alive / 26 gold
- SOCKS4: 210 alive / 130 gold
- SOCKS5: 252 alive / 133 gold

## Historical pool

- Discovered: 144740
- Ever alive: 25049
- Ever gold: 1053

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
