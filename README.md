# SyndProxy private pool

## Current pool

- Alive now: 1006
- Gold now: 369
- HTTP: 347 alive / 69 gold
- HTTPS: 206 alive / 20 gold
- SOCKS4: 206 alive / 120 gold
- SOCKS5: 247 alive / 160 gold

## Historical pool

- Discovered: 148333
- Ever alive: 26106
- Ever gold: 1079

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
