# SyndProxy private pool

## Current pool

- Alive now: 1372
- Gold now: 407
- HTTP: 507 alive / 79 gold
- HTTPS: 316 alive / 16 gold
- SOCKS4: 241 alive / 157 gold
- SOCKS5: 308 alive / 155 gold

## Historical pool

- Discovered: 134523
- Ever alive: 21911
- Ever gold: 888

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
