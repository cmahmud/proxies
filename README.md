# SyndProxy private pool

## Current pool

- Alive now: 686
- Gold now: 364
- HTTP: 177 alive / 67 gold
- HTTPS: 136 alive / 21 gold
- SOCKS4: 189 alive / 135 gold
- SOCKS5: 184 alive / 141 gold

## Historical pool

- Discovered: 149497
- Ever alive: 26674
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
