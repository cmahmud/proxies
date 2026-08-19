# SyndProxy private pool

## Current pool

- Alive now: 1079
- Gold now: 531
- HTTP: 387 alive / 165 gold
- HTTPS: 251 alive / 93 gold
- SOCKS4: 234 alive / 149 gold
- SOCKS5: 207 alive / 124 gold

## Historical pool

- Discovered: 123229
- Ever alive: 18976
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
