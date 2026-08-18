# SyndProxy private pool

## Current pool

- Alive now: 985
- Gold now: 240
- HTTP: 391 alive / 37 gold
- HTTPS: 158 alive / 8 gold
- SOCKS4: 235 alive / 131 gold
- SOCKS5: 201 alive / 64 gold

## Historical pool

- Discovered: 94344
- Ever alive: 9652
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
