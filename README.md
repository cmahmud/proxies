# SyndProxy private pool

## Current pool

- Alive now: 1114
- Gold now: 470
- HTTP: 405 alive / 121 gold
- HTTPS: 252 alive / 73 gold
- SOCKS4: 233 alive / 136 gold
- SOCKS5: 224 alive / 140 gold

## Historical pool

- Discovered: 113536
- Ever alive: 16581
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
