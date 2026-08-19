# SyndProxy private pool

## Current pool

- Alive now: 980
- Gold now: 465
- HTTP: 338 alive / 136 gold
- HTTPS: 240 alive / 91 gold
- SOCKS4: 202 alive / 128 gold
- SOCKS5: 200 alive / 110 gold

## Historical pool

- Discovered: 117111
- Ever alive: 17382
- Ever gold: 663

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
