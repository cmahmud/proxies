# SyndProxy private pool

## Current pool

- Alive now: 1155
- Gold now: 470
- HTTP: 403 alive / 119 gold
- HTTPS: 272 alive / 75 gold
- SOCKS4: 232 alive / 141 gold
- SOCKS5: 248 alive / 135 gold

## Historical pool

- Discovered: 113536
- Ever alive: 16480
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
