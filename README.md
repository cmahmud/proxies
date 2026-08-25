# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 431
- HTTP: 128 alive / 76 gold
- HTTPS: 69 alive / 24 gold
- SOCKS4: 166 alive / 161 gold
- SOCKS5: 185 alive / 170 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34785
- Ever gold: 1258

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
