# SyndProxy private pool

## Current pool

- Alive now: 1079
- Gold now: 531
- HTTP: 378 alive / 162 gold
- HTTPS: 261 alive / 95 gold
- SOCKS4: 233 alive / 146 gold
- SOCKS5: 207 alive / 128 gold

## Historical pool

- Discovered: 123227
- Ever alive: 18966
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
