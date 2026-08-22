# SyndProxy private pool

## Current pool

- Alive now: 788
- Gold now: 396
- HTTP: 198 alive / 88 gold
- HTTPS: 142 alive / 31 gold
- SOCKS4: 198 alive / 126 gold
- SOCKS5: 250 alive / 151 gold

## Historical pool

- Discovered: 163842
- Ever alive: 31925
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
