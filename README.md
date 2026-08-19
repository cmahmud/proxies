# SyndProxy private pool

## Current pool

- Alive now: 1160
- Gold now: 387
- HTTP: 395 alive / 84 gold
- HTTPS: 293 alive / 13 gold
- SOCKS4: 219 alive / 127 gold
- SOCKS5: 253 alive / 163 gold

## Historical pool

- Discovered: 131855
- Ever alive: 21313
- Ever gold: 880

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
