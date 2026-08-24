# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 438
- HTTP: 139 alive / 82 gold
- HTTPS: 114 alive / 25 gold
- SOCKS4: 183 alive / 161 gold
- SOCKS5: 193 alive / 170 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34564
- Ever gold: 1256

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
