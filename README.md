# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 419
- HTTP: 87 alive / 67 gold
- HTTPS: 75 alive / 23 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 183 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 37006
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
