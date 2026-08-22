# SyndProxy private pool

## Current pool

- Alive now: 865
- Gold now: 405
- HTTP: 230 alive / 88 gold
- HTTPS: 165 alive / 27 gold
- SOCKS4: 223 alive / 134 gold
- SOCKS5: 247 alive / 156 gold

## Historical pool

- Discovered: 162771
- Ever alive: 31654
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
