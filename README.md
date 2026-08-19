# SyndProxy private pool

## Current pool

- Alive now: 1072
- Gold now: 470
- HTTP: 365 alive / 121 gold
- HTTPS: 259 alive / 73 gold
- SOCKS4: 225 alive / 137 gold
- SOCKS5: 223 alive / 139 gold

## Historical pool

- Discovered: 113536
- Ever alive: 16581
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
