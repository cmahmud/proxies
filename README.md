# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 420
- HTTP: 114 alive / 71 gold
- HTTPS: 75 alive / 21 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 189 alive / 168 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34802
- Ever gold: 1258

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
