# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 401
- HTTP: 161 alive / 70 gold
- HTTPS: 76 alive / 13 gold
- SOCKS4: 188 alive / 156 gold
- SOCKS5: 204 alive / 162 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33304
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
