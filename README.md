# SyndProxy private pool

## Current pool

- Alive now: 782
- Gold now: 401
- HTTP: 213 alive / 82 gold
- HTTPS: 126 alive / 16 gold
- SOCKS4: 205 alive / 146 gold
- SOCKS5: 238 alive / 157 gold

## Historical pool

- Discovered: 155790
- Ever alive: 29316
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
