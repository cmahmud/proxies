# SyndProxy private pool

## Current pool

- Alive now: 1144
- Gold now: 475
- HTTP: 417 alive / 123 gold
- HTTPS: 270 alive / 70 gold
- SOCKS4: 232 alive / 141 gold
- SOCKS5: 225 alive / 141 gold

## Historical pool

- Discovered: 113536
- Ever alive: 16536
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
