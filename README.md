# SyndProxy private pool

## Current pool

- Alive now: 967
- Gold now: 373
- HTTP: 287 alive / 65 gold
- HTTPS: 238 alive / 19 gold
- SOCKS4: 201 alive / 128 gold
- SOCKS5: 241 alive / 161 gold

## Historical pool

- Discovered: 110416
- Ever alive: 15723
- Ever gold: 503

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
