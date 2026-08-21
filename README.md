# SyndProxy private pool

## Current pool

- Alive now: 1029
- Gold now: 396
- HTTP: 346 alive / 108 gold
- HTTPS: 254 alive / 23 gold
- SOCKS4: 205 alive / 143 gold
- SOCKS5: 224 alive / 122 gold

## Historical pool

- Discovered: 153184
- Ever alive: 28502
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
