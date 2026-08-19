# SyndProxy private pool

## Current pool

- Alive now: 1155
- Gold now: 393
- HTTP: 391 alive / 84 gold
- HTTPS: 233 alive / 17 gold
- SOCKS4: 236 alive / 146 gold
- SOCKS5: 295 alive / 146 gold

## Historical pool

- Discovered: 133968
- Ever alive: 21763
- Ever gold: 887

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
