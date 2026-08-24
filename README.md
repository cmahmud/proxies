# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 398
- HTTP: 104 alive / 61 gold
- HTTPS: 39 alive / 13 gold
- SOCKS4: 166 alive / 158 gold
- SOCKS5: 187 alive / 166 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33657
- Ever gold: 1247

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
