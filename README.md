# SyndProxy private pool

## Current pool

- Alive now: 1010
- Gold now: 530
- HTTP: 343 alive / 165 gold
- HTTPS: 230 alive / 90 gold
- SOCKS4: 230 alive / 147 gold
- SOCKS5: 207 alive / 128 gold

## Historical pool

- Discovered: 123235
- Ever alive: 19016
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
