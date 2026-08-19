# SyndProxy private pool

## Current pool

- Alive now: 992
- Gold now: 546
- HTTP: 351 alive / 171 gold
- HTTPS: 231 alive / 89 gold
- SOCKS4: 210 alive / 149 gold
- SOCKS5: 200 alive / 137 gold

## Historical pool

- Discovered: 123235
- Ever alive: 19037
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
