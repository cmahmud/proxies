# SyndProxy private pool

## Current pool

- Alive now: 1195
- Gold now: 394
- HTTP: 393 alive / 87 gold
- HTTPS: 279 alive / 20 gold
- SOCKS4: 230 alive / 136 gold
- SOCKS5: 293 alive / 151 gold

## Historical pool

- Discovered: 134558
- Ever alive: 22165
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
