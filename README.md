# SyndProxy private pool

## Current pool

- Alive now: 1046
- Gold now: 389
- HTTP: 319 alive / 98 gold
- HTTPS: 211 alive / 23 gold
- SOCKS4: 249 alive / 132 gold
- SOCKS5: 267 alive / 136 gold

## Historical pool

- Discovered: 144740
- Ever alive: 25081
- Ever gold: 1054

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
