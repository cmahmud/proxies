# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 436
- HTTP: 121 alive / 79 gold
- HTTPS: 71 alive / 25 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 186 alive / 171 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34695
- Ever gold: 1258

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
