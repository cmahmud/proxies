# SyndProxy private pool

## Current pool

- Alive now: 1069
- Gold now: 400
- HTTP: 358 alive / 85 gold
- HTTPS: 244 alive / 24 gold
- SOCKS4: 222 alive / 149 gold
- SOCKS5: 245 alive / 142 gold

## Historical pool

- Discovered: 165751
- Ever alive: 32287
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
