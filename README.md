# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 399
- HTTP: 101 alive / 61 gold
- HTTPS: 41 alive / 13 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 187 alive / 167 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33657
- Ever gold: 1247

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
