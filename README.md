# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 402
- HTTP: 102 alive / 70 gold
- HTTPS: 81 alive / 15 gold
- SOCKS4: 164 alive / 153 gold
- SOCKS5: 191 alive / 164 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34834
- Ever gold: 1258

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
