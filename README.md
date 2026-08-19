# SyndProxy private pool

## Current pool

- Alive now: 1156
- Gold now: 396
- HTTP: 380 alive / 92 gold
- HTTPS: 257 alive / 13 gold
- SOCKS4: 236 alive / 140 gold
- SOCKS5: 283 alive / 151 gold

## Historical pool

- Discovered: 131828
- Ever alive: 21067
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
