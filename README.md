# SyndProxy private pool

## Current pool

- Alive now: 1042
- Gold now: 401
- HTTP: 348 alive / 87 gold
- HTTPS: 245 alive / 27 gold
- SOCKS4: 223 alive / 149 gold
- SOCKS5: 226 alive / 138 gold

## Historical pool

- Discovered: 165822
- Ever alive: 32338
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
