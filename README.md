# SyndProxy private pool

## Current pool

- Alive now: 1248
- Gold now: 529
- HTTP: 459 alive / 185 gold
- HTTPS: 348 alive / 63 gold
- SOCKS4: 206 alive / 122 gold
- SOCKS5: 235 alive / 159 gold

## Historical pool

- Discovered: 125667
- Ever alive: 19605
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
