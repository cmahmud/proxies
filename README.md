# SyndProxy private pool

## Current pool

- Alive now: 773
- Gold now: 366
- HTTP: 196 alive / 87 gold
- HTTPS: 152 alive / 20 gold
- SOCKS4: 217 alive / 132 gold
- SOCKS5: 208 alive / 127 gold

## Historical pool

- Discovered: 149497
- Ever alive: 26613
- Ever gold: 1084

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
