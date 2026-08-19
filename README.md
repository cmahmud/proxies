# SyndProxy private pool

## Current pool

- Alive now: 1252
- Gold now: 397
- HTTP: 404 alive / 90 gold
- HTTPS: 289 alive / 11 gold
- SOCKS4: 264 alive / 141 gold
- SOCKS5: 295 alive / 155 gold

## Historical pool

- Discovered: 131826
- Ever alive: 21036
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
