# SyndProxy private pool

## Current pool

- Alive now: 1062
- Gold now: 408
- HTTP: 357 alive / 91 gold
- HTTPS: 253 alive / 34 gold
- SOCKS4: 215 alive / 146 gold
- SOCKS5: 237 alive / 137 gold

## Historical pool

- Discovered: 160997
- Ever alive: 30969
- Ever gold: 1152

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
