# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 438
- HTTP: 151 alive / 83 gold
- HTTPS: 49 alive / 24 gold
- SOCKS4: 187 alive / 158 gold
- SOCKS5: 187 alive / 173 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34732
- Ever gold: 1258

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
