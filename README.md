# SyndProxy validated proxy pool

## Current pool

- Alive now: 555
- Gold now: 434
- HTTP: 134 alive / 80 gold
- HTTPS: 61 alive / 24 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 185 alive / 170 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34132
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
