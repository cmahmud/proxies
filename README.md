# SyndProxy private pool

## Current pool

- Alive now: 975
- Gold now: 548
- HTTP: 343 alive / 173 gold
- HTTPS: 231 alive / 89 gold
- SOCKS4: 207 alive / 149 gold
- SOCKS5: 194 alive / 137 gold

## Historical pool

- Discovered: 123235
- Ever alive: 19035
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
