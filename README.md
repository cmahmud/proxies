# SyndProxy private pool

## Current pool

- Alive now: 1299
- Gold now: 562
- HTTP: 470 alive / 190 gold
- HTTPS: 363 alive / 93 gold
- SOCKS4: 250 alive / 146 gold
- SOCKS5: 216 alive / 133 gold

## Historical pool

- Discovered: 136930
- Ever alive: 22909
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
