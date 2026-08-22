# SyndProxy private pool

## Current pool

- Alive now: 803
- Gold now: 399
- HTTP: 218 alive / 87 gold
- HTTPS: 150 alive / 29 gold
- SOCKS4: 200 alive / 130 gold
- SOCKS5: 235 alive / 153 gold

## Historical pool

- Discovered: 163842
- Ever alive: 31926
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
