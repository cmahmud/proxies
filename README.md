# SyndProxy private pool

## Current pool

- Alive now: 1069
- Gold now: 522
- HTTP: 368 alive / 156 gold
- HTTPS: 251 alive / 94 gold
- SOCKS4: 238 alive / 146 gold
- SOCKS5: 212 alive / 126 gold

## Historical pool

- Discovered: 123226
- Ever alive: 18920
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
