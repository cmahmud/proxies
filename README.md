# SyndProxy validated proxy pool

## Current pool

- Alive now: 601
- Gold now: 437
- HTTP: 150 alive / 83 gold
- HTTPS: 78 alive / 23 gold
- SOCKS4: 186 alive / 159 gold
- SOCKS5: 187 alive / 172 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34748
- Ever gold: 1258

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
