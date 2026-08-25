# SyndProxy validated proxy pool

## Current pool

- Alive now: 563
- Gold now: 423
- HTTP: 116 alive / 72 gold
- HTTPS: 89 alive / 22 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 189 alive / 168 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34801
- Ever gold: 1258

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
