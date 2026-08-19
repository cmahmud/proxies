# SyndProxy private pool

## Current pool

- Alive now: 985
- Gold now: 544
- HTTP: 338 alive / 174 gold
- HTTPS: 242 alive / 89 gold
- SOCKS4: 214 alive / 146 gold
- SOCKS5: 191 alive / 135 gold

## Historical pool

- Discovered: 123235
- Ever alive: 19033
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
