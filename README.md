# SyndProxy private pool

## Current pool

- Alive now: 1061
- Gold now: 376
- HTTP: 316 alive / 73 gold
- HTTPS: 269 alive / 17 gold
- SOCKS4: 222 alive / 125 gold
- SOCKS5: 254 alive / 161 gold

## Historical pool

- Discovered: 110856
- Ever alive: 15894
- Ever gold: 506

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
