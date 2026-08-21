# SyndProxy private pool

## Current pool

- Alive now: 1000
- Gold now: 403
- HTTP: 329 alive / 100 gold
- HTTPS: 247 alive / 28 gold
- SOCKS4: 185 alive / 121 gold
- SOCKS5: 239 alive / 154 gold

## Historical pool

- Discovered: 152759
- Ever alive: 28350
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
