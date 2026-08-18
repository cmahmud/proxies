# SyndProxy private pool

## Current pool

- Alive now: 969
- Gold now: 294
- HTTP: 279 alive / 24 gold
- HTTPS: 199 alive / 4 gold
- SOCKS4: 248 alive / 147 gold
- SOCKS5: 243 alive / 119 gold

## Historical pool

- Discovered: 102809
- Ever alive: 12765
- Ever gold: 400

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
