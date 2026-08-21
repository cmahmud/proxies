# SyndProxy private pool

## Current pool

- Alive now: 1008
- Gold now: 400
- HTTP: 315 alive / 98 gold
- HTTPS: 240 alive / 23 gold
- SOCKS4: 208 alive / 135 gold
- SOCKS5: 245 alive / 144 gold

## Historical pool

- Discovered: 152753
- Ever alive: 28262
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
