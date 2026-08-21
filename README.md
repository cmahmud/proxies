# SyndProxy private pool

## Current pool

- Alive now: 1134
- Gold now: 411
- HTTP: 407 alive / 105 gold
- HTTPS: 242 alive / 24 gold
- SOCKS4: 216 alive / 132 gold
- SOCKS5: 269 alive / 150 gold

## Historical pool

- Discovered: 152217
- Ever alive: 27966
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
