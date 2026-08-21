# SyndProxy private pool

## Current pool

- Alive now: 1009
- Gold now: 431
- HTTP: 301 alive / 96 gold
- HTTPS: 189 alive / 24 gold
- SOCKS4: 239 alive / 146 gold
- SOCKS5: 280 alive / 165 gold

## Historical pool

- Discovered: 152749
- Ever alive: 28163
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
