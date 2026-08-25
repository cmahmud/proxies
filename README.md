# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 417
- HTTP: 119 alive / 69 gold
- HTTPS: 71 alive / 20 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 184 alive / 167 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35379
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
