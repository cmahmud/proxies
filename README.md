# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 420
- HTTP: 110 alive / 71 gold
- HTTPS: 66 alive / 20 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 189 alive / 169 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34805
- Ever gold: 1258

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
