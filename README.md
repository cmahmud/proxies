# SyndProxy private pool

## Current pool

- Alive now: 1033
- Gold now: 525
- HTTP: 366 alive / 162 gold
- HTTPS: 254 alive / 93 gold
- SOCKS4: 210 alive / 149 gold
- SOCKS5: 203 alive / 121 gold

## Historical pool

- Discovered: 123229
- Ever alive: 18994
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
