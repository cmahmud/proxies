# SyndProxy private pool

## Current pool

- Alive now: 1030
- Gold now: 428
- HTTP: 337 alive / 85 gold
- HTTPS: 204 alive / 29 gold
- SOCKS4: 221 alive / 154 gold
- SOCKS5: 268 alive / 160 gold

## Historical pool

- Discovered: 159260
- Ever alive: 30230
- Ever gold: 1143

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
