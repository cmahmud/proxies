# SyndProxy private pool

## Current pool

- Alive now: 882
- Gold now: 400
- HTTP: 260 alive / 88 gold
- HTTPS: 218 alive / 24 gold
- SOCKS4: 195 alive / 132 gold
- SOCKS5: 209 alive / 156 gold

## Historical pool

- Discovered: 151057
- Ever alive: 27251
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
