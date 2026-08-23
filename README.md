# SyndProxy validated proxy pool

## Current pool

- Alive now: 665
- Gold now: 347
- HTTP: 226 alive / 38 gold
- HTTPS: 44 alive / 10 gold
- SOCKS4: 180 alive / 154 gold
- SOCKS5: 215 alive / 145 gold

## Historical pool

- Discovered: 171094
- Ever alive: 32869
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
