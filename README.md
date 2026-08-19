# SyndProxy private pool

## Current pool

- Alive now: 967
- Gold now: 543
- HTTP: 340 alive / 167 gold
- HTTPS: 223 alive / 90 gold
- SOCKS4: 209 alive / 150 gold
- SOCKS5: 195 alive / 136 gold

## Historical pool

- Discovered: 123235
- Ever alive: 19040
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
