# SyndProxy private pool

## Current pool

- Alive now: 878
- Gold now: 384
- HTTP: 269 alive / 88 gold
- HTTPS: 167 alive / 20 gold
- SOCKS4: 181 alive / 117 gold
- SOCKS5: 261 alive / 159 gold

## Historical pool

- Discovered: 166336
- Ever alive: 32396
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
