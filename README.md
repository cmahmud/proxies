# SyndProxy private pool

## Current pool

- Alive now: 1174
- Gold now: 474
- HTTP: 436 alive / 123 gold
- HTTPS: 286 alive / 70 gold
- SOCKS4: 227 alive / 140 gold
- SOCKS5: 225 alive / 141 gold

## Historical pool

- Discovered: 113536
- Ever alive: 16536
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
