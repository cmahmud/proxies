# SyndProxy private pool

## Current pool

- Alive now: 1032
- Gold now: 528
- HTTP: 363 alive / 163 gold
- HTTPS: 252 alive / 94 gold
- SOCKS4: 210 alive / 149 gold
- SOCKS5: 207 alive / 122 gold

## Historical pool

- Discovered: 123229
- Ever alive: 18994
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
