# SyndProxy private pool

## Current pool

- Alive now: 965
- Gold now: 403
- HTTP: 286 alive / 97 gold
- HTTPS: 223 alive / 24 gold
- SOCKS4: 212 alive / 136 gold
- SOCKS5: 244 alive / 146 gold

## Historical pool

- Discovered: 152753
- Ever alive: 28250
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
