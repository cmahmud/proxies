# SyndProxy private pool

## Current pool

- Alive now: 1269
- Gold now: 511
- HTTP: 471 alive / 164 gold
- HTTPS: 337 alive / 48 gold
- SOCKS4: 217 alive / 141 gold
- SOCKS5: 244 alive / 158 gold

## Historical pool

- Discovered: 125672
- Ever alive: 19665
- Ever gold: 775

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
