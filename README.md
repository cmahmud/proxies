# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 403
- HTTP: 99 alive / 70 gold
- HTTPS: 66 alive / 15 gold
- SOCKS4: 164 alive / 153 gold
- SOCKS5: 190 alive / 165 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34841
- Ever gold: 1258

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
