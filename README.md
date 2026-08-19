# SyndProxy private pool

## Current pool

- Alive now: 982
- Gold now: 532
- HTTP: 336 alive / 165 gold
- HTTPS: 225 alive / 91 gold
- SOCKS4: 222 alive / 147 gold
- SOCKS5: 199 alive / 129 gold

## Historical pool

- Discovered: 123235
- Ever alive: 19016
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
