# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 406
- HTTP: 99 alive / 71 gold
- HTTPS: 89 alive / 16 gold
- SOCKS4: 166 alive / 154 gold
- SOCKS5: 193 alive / 165 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34854
- Ever gold: 1258

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
