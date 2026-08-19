# SyndProxy private pool

## Current pool

- Alive now: 1108
- Gold now: 474
- HTTP: 395 alive / 120 gold
- HTTPS: 272 alive / 72 gold
- SOCKS4: 223 alive / 140 gold
- SOCKS5: 218 alive / 142 gold

## Historical pool

- Discovered: 113536
- Ever alive: 16543
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
