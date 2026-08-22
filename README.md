# SyndProxy private pool

## Current pool

- Alive now: 934
- Gold now: 403
- HTTP: 288 alive / 89 gold
- HTTPS: 215 alive / 28 gold
- SOCKS4: 206 alive / 149 gold
- SOCKS5: 225 alive / 137 gold

## Historical pool

- Discovered: 165822
- Ever alive: 32341
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
