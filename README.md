# SyndProxy private pool

## Current pool

- Alive now: 1095
- Gold now: 443
- HTTP: 379 alive / 106 gold
- HTTPS: 274 alive / 36 gold
- SOCKS4: 205 alive / 140 gold
- SOCKS5: 237 alive / 161 gold

## Historical pool

- Discovered: 152761
- Ever alive: 28373
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
