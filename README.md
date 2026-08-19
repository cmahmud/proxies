# SyndProxy private pool

## Current pool

- Alive now: 1040
- Gold now: 526
- HTTP: 372 alive / 159 gold
- HTTPS: 246 alive / 94 gold
- SOCKS4: 214 alive / 149 gold
- SOCKS5: 208 alive / 124 gold

## Historical pool

- Discovered: 123229
- Ever alive: 18990
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
