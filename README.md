# SyndProxy private pool

## Current pool

- Alive now: 1060
- Gold now: 522
- HTTP: 366 alive / 157 gold
- HTTPS: 244 alive / 93 gold
- SOCKS4: 238 alive / 145 gold
- SOCKS5: 212 alive / 127 gold

## Historical pool

- Discovered: 123226
- Ever alive: 18920
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
