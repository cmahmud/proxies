# SyndProxy private pool

## Current pool

- Alive now: 932
- Gold now: 315
- HTTP: 293 alive / 40 gold
- HTTPS: 186 alive / 9 gold
- SOCKS4: 233 alive / 134 gold
- SOCKS5: 220 alive / 132 gold

## Historical pool

- Discovered: 107013
- Ever alive: 14270
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
