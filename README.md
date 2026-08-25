# SyndProxy validated proxy pool

## Current pool

- Alive now: 567
- Gold now: 427
- HTTP: 121 alive / 75 gold
- HTTPS: 91 alive / 23 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 187 alive / 168 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34798
- Ever gold: 1258

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
