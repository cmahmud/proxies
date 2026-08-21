# SyndProxy private pool

## Current pool

- Alive now: 927
- Gold now: 405
- HTTP: 262 alive / 88 gold
- HTTPS: 193 alive / 24 gold
- SOCKS4: 230 alive / 146 gold
- SOCKS5: 242 alive / 147 gold

## Historical pool

- Discovered: 154723
- Ever alive: 29096
- Ever gold: 1123

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
