# SyndProxy validated proxy pool

## Current pool

- Alive now: 589
- Gold now: 437
- HTTP: 158 alive / 82 gold
- HTTPS: 54 alive / 24 gold
- SOCKS4: 188 alive / 159 gold
- SOCKS5: 189 alive / 172 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34732
- Ever gold: 1258

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
