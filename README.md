# SyndProxy private pool

## Current pool

- Alive now: 1109
- Gold now: 420
- HTTP: 391 alive / 106 gold
- HTTPS: 288 alive / 35 gold
- SOCKS4: 191 alive / 124 gold
- SOCKS5: 239 alive / 155 gold

## Historical pool

- Discovered: 152761
- Ever alive: 28366
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
