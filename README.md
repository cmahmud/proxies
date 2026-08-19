# SyndProxy private pool

## Current pool

- Alive now: 1341
- Gold now: 436
- HTTP: 470 alive / 98 gold
- HTTPS: 308 alive / 26 gold
- SOCKS4: 247 alive / 148 gold
- SOCKS5: 316 alive / 164 gold

## Historical pool

- Discovered: 136220
- Ever alive: 22453
- Ever gold: 901

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
