# SyndProxy private pool

## Current pool

- Alive now: 777
- Gold now: 260
- HTTP: 269 alive / 30 gold
- HTTPS: 101 alive / 8 gold
- SOCKS4: 200 alive / 133 gold
- SOCKS5: 207 alive / 89 gold

## Historical pool

- Discovered: 91741
- Ever alive: 9280
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
