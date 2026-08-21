# SyndProxy private pool

## Current pool

- Alive now: 1088
- Gold now: 439
- HTTP: 390 alive / 104 gold
- HTTPS: 240 alive / 25 gold
- SOCKS4: 207 alive / 144 gold
- SOCKS5: 251 alive / 166 gold

## Historical pool

- Discovered: 152765
- Ever alive: 28401
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
