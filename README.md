# SyndProxy private pool

## Current pool

- Alive now: 1219
- Gold now: 534
- HTTP: 466 alive / 155 gold
- HTTPS: 327 alive / 108 gold
- SOCKS4: 233 alive / 142 gold
- SOCKS5: 193 alive / 129 gold

## Historical pool

- Discovered: 127372
- Ever alive: 19945
- Ever gold: 804

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
