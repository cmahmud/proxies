# SyndProxy private pool

## Current pool

- Alive now: 904
- Gold now: 262
- HTTP: 279 alive / 32 gold
- HTTPS: 177 alive / 4 gold
- SOCKS4: 242 alive / 129 gold
- SOCKS5: 206 alive / 97 gold

## Historical pool

- Discovered: 95396
- Ever alive: 10616
- Ever gold: 378

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
