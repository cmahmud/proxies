# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 410
- HTTP: 103 alive / 70 gold
- HTTPS: 86 alive / 15 gold
- SOCKS4: 166 alive / 157 gold
- SOCKS5: 192 alive / 168 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34834
- Ever gold: 1258

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
