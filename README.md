# SyndProxy private pool

## Current pool

- Alive now: 1133
- Gold now: 467
- HTTP: 394 alive / 119 gold
- HTTPS: 269 alive / 72 gold
- SOCKS4: 238 alive / 136 gold
- SOCKS5: 232 alive / 140 gold

## Historical pool

- Discovered: 113536
- Ever alive: 16569
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
