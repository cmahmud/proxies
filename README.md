# SyndProxy private pool

## Current pool

- Alive now: 686
- Gold now: 203
- HTTP: 158 alive / 23 gold
- HTTPS: 118 alive / 9 gold
- SOCKS4: 210 alive / 90 gold
- SOCKS5: 200 alive / 81 gold

## Historical pool

- Discovered: 87994
- Ever alive: 7995
- Ever gold: 343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
