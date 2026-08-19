# SyndProxy private pool

## Current pool

- Alive now: 1103
- Gold now: 469
- HTTP: 396 alive / 119 gold
- HTTPS: 249 alive / 73 gold
- SOCKS4: 229 alive / 137 gold
- SOCKS5: 229 alive / 140 gold

## Historical pool

- Discovered: 113536
- Ever alive: 16581
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
