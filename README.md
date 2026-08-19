# SyndProxy private pool

## Current pool

- Alive now: 961
- Gold now: 543
- HTTP: 340 alive / 173 gold
- HTTPS: 228 alive / 89 gold
- SOCKS4: 203 alive / 146 gold
- SOCKS5: 190 alive / 135 gold

## Historical pool

- Discovered: 123235
- Ever alive: 19035
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
