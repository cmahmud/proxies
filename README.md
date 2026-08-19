# SyndProxy private pool

## Current pool

- Alive now: 1058
- Gold now: 534
- HTTP: 373 alive / 159 gold
- HTTPS: 248 alive / 94 gold
- SOCKS4: 229 alive / 146 gold
- SOCKS5: 208 alive / 135 gold

## Historical pool

- Discovered: 123170
- Ever alive: 18876
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
