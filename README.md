# SyndProxy validated proxy pool

## Current pool

- Alive now: 603
- Gold now: 439
- HTTP: 161 alive / 83 gold
- HTTPS: 64 alive / 24 gold
- SOCKS4: 189 alive / 160 gold
- SOCKS5: 189 alive / 172 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34732
- Ever gold: 1258

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
