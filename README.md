# SyndProxy private pool

## Current pool

- Alive now: 941
- Gold now: 331
- HTTP: 279 alive / 58 gold
- HTTPS: 201 alive / 9 gold
- SOCKS4: 237 alive / 142 gold
- SOCKS5: 224 alive / 122 gold

## Historical pool

- Discovered: 129272
- Ever alive: 20262
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
