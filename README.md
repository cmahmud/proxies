# SyndProxy private pool

## Current pool

- Alive now: 1104
- Gold now: 538
- HTTP: 410 alive / 164 gold
- HTTPS: 270 alive / 89 gold
- SOCKS4: 225 alive / 149 gold
- SOCKS5: 199 alive / 136 gold

## Historical pool

- Discovered: 123235
- Ever alive: 19083
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
