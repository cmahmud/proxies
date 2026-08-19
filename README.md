# SyndProxy private pool

## Current pool

- Alive now: 1032
- Gold now: 532
- HTTP: 369 alive / 164 gold
- HTTPS: 238 alive / 92 gold
- SOCKS4: 215 alive / 150 gold
- SOCKS5: 210 alive / 126 gold

## Historical pool

- Discovered: 123229
- Ever alive: 18987
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
