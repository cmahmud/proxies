# SyndProxy private pool

## Current pool

- Alive now: 797
- Gold now: 351
- HTTP: 203 alive / 72 gold
- HTTPS: 178 alive / 20 gold
- SOCKS4: 209 alive / 134 gold
- SOCKS5: 207 alive / 125 gold

## Historical pool

- Discovered: 149501
- Ever alive: 26713
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
