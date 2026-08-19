# SyndProxy private pool

## Current pool

- Alive now: 1139
- Gold now: 466
- HTTP: 396 alive / 120 gold
- HTTPS: 272 alive / 72 gold
- SOCKS4: 239 alive / 141 gold
- SOCKS5: 232 alive / 133 gold

## Historical pool

- Discovered: 113536
- Ever alive: 16520
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
