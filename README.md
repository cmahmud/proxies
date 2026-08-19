# SyndProxy private pool

## Current pool

- Alive now: 999
- Gold now: 537
- HTTP: 345 alive / 170 gold
- HTTPS: 230 alive / 89 gold
- SOCKS4: 224 alive / 144 gold
- SOCKS5: 200 alive / 134 gold

## Historical pool

- Discovered: 123235
- Ever alive: 19017
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
