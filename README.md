# SyndProxy validated proxy pool

## Current pool

- Alive now: 588
- Gold now: 433
- HTTP: 124 alive / 78 gold
- HTTPS: 97 alive / 26 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 187 alive / 168 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34660
- Ever gold: 1257

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
