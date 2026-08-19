# SyndProxy private pool

## Current pool

- Alive now: 1019
- Gold now: 543
- HTTP: 342 alive / 166 gold
- HTTPS: 268 alive / 90 gold
- SOCKS4: 215 alive / 150 gold
- SOCKS5: 194 alive / 137 gold

## Historical pool

- Discovered: 123235
- Ever alive: 19059
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
