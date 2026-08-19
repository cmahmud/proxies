# SyndProxy private pool

## Current pool

- Alive now: 1073
- Gold now: 542
- HTTP: 377 alive / 162 gold
- HTTPS: 249 alive / 94 gold
- SOCKS4: 238 alive / 145 gold
- SOCKS5: 209 alive / 141 gold

## Historical pool

- Discovered: 123170
- Ever alive: 18874
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
