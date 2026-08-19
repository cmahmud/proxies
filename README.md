# SyndProxy private pool

## Current pool

- Alive now: 1036
- Gold now: 370
- HTTP: 359 alive / 71 gold
- HTTPS: 240 alive / 17 gold
- SOCKS4: 200 alive / 123 gold
- SOCKS5: 237 alive / 159 gold

## Historical pool

- Discovered: 110856
- Ever alive: 15764
- Ever gold: 504

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
