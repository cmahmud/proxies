# SyndProxy private pool

## Current pool

- Alive now: 1041
- Gold now: 403
- HTTP: 356 alive / 86 gold
- HTTPS: 204 alive / 29 gold
- SOCKS4: 230 alive / 134 gold
- SOCKS5: 251 alive / 154 gold

## Historical pool

- Discovered: 166609
- Ever alive: 32422
- Ever gold: 1180

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
