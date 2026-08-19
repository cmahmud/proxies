# SyndProxy private pool

## Current pool

- Alive now: 1249
- Gold now: 386
- HTTP: 411 alive / 91 gold
- HTTPS: 274 alive / 19 gold
- SOCKS4: 254 alive / 138 gold
- SOCKS5: 310 alive / 138 gold

## Historical pool

- Discovered: 133938
- Ever alive: 21485
- Ever gold: 884

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
