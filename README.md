# SyndProxy private pool

## Current pool

- Alive now: 1008
- Gold now: 542
- HTTP: 353 alive / 173 gold
- HTTPS: 244 alive / 88 gold
- SOCKS4: 217 alive / 146 gold
- SOCKS5: 194 alive / 135 gold

## Historical pool

- Discovered: 123235
- Ever alive: 19033
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
