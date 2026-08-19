# SyndProxy private pool

## Current pool

- Alive now: 1058
- Gold now: 538
- HTTP: 372 alive / 160 gold
- HTTPS: 248 alive / 94 gold
- SOCKS4: 233 alive / 148 gold
- SOCKS5: 205 alive / 136 gold

## Historical pool

- Discovered: 123170
- Ever alive: 18879
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
