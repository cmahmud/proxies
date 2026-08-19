# SyndProxy private pool

## Current pool

- Alive now: 962
- Gold now: 359
- HTTP: 312 alive / 71 gold
- HTTPS: 214 alive / 13 gold
- SOCKS4: 214 alive / 128 gold
- SOCKS5: 222 alive / 147 gold

## Historical pool

- Discovered: 129290
- Ever alive: 20336
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
