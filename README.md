# SyndProxy private pool

## Current pool

- Alive now: 1162
- Gold now: 473
- HTTP: 431 alive / 123 gold
- HTTPS: 278 alive / 70 gold
- SOCKS4: 226 alive / 140 gold
- SOCKS5: 227 alive / 140 gold

## Historical pool

- Discovered: 113536
- Ever alive: 16536
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
