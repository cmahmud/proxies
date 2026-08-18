# SyndProxy private pool

## Current pool

- Alive now: 806
- Gold now: 286
- HTTP: 204 alive / 25 gold
- HTTPS: 150 alive / 5 gold
- SOCKS4: 230 alive / 144 gold
- SOCKS5: 222 alive / 112 gold

## Historical pool

- Discovered: 99165
- Ever alive: 12351
- Ever gold: 396

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
