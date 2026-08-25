# SyndProxy validated proxy pool

## Current pool

- Alive now: 583
- Gold now: 429
- HTTP: 110 alive / 66 gold
- HTTPS: 86 alive / 24 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 206 alive / 178 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35926
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
