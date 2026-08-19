# SyndProxy private pool

## Current pool

- Alive now: 1170
- Gold now: 473
- HTTP: 437 alive / 119 gold
- HTTPS: 276 alive / 72 gold
- SOCKS4: 231 alive / 140 gold
- SOCKS5: 226 alive / 142 gold

## Historical pool

- Discovered: 113536
- Ever alive: 16536
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
