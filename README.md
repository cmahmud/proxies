# SyndProxy private pool

## Current pool

- Alive now: 825
- Gold now: 367
- HTTP: 223 alive / 72 gold
- HTTPS: 183 alive / 20 gold
- SOCKS4: 204 alive / 134 gold
- SOCKS5: 215 alive / 141 gold

## Historical pool

- Discovered: 149501
- Ever alive: 26711
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
