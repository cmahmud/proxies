# SyndProxy private pool

## Current pool

- Alive now: 1166
- Gold now: 541
- HTTP: 437 alive / 163 gold
- HTTPS: 292 alive / 89 gold
- SOCKS4: 224 alive / 145 gold
- SOCKS5: 213 alive / 144 gold

## Historical pool

- Discovered: 123921
- Ever alive: 19140
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
