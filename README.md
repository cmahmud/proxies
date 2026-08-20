# SyndProxy private pool

## Current pool

- Alive now: 777
- Gold now: 365
- HTTP: 214 alive / 71 gold
- HTTPS: 156 alive / 18 gold
- SOCKS4: 196 alive / 134 gold
- SOCKS5: 211 alive / 142 gold

## Historical pool

- Discovered: 149501
- Ever alive: 26703
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
