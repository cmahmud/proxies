# SyndProxy validated proxy pool

## Current pool

- Alive now: 555
- Gold now: 428
- HTTP: 130 alive / 76 gold
- HTTPS: 73 alive / 23 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 185 alive / 170 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34780
- Ever gold: 1258

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
