# SyndProxy private pool

## Current pool

- Alive now: 1137
- Gold now: 468
- HTTP: 387 alive / 118 gold
- HTTPS: 270 alive / 74 gold
- SOCKS4: 237 alive / 141 gold
- SOCKS5: 243 alive / 135 gold

## Historical pool

- Discovered: 113536
- Ever alive: 16469
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
