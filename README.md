# SyndProxy private pool

## Current pool

- Alive now: 1155
- Gold now: 465
- HTTP: 415 alive / 125 gold
- HTTPS: 321 alive / 74 gold
- SOCKS4: 210 alive / 139 gold
- SOCKS5: 209 alive / 127 gold

## Historical pool

- Discovered: 113547
- Ever alive: 16710
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
