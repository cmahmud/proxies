# SyndProxy private pool

## Current pool

- Alive now: 1230
- Gold now: 590
- HTTP: 444 alive / 190 gold
- HTTPS: 328 alive / 98 gold
- SOCKS4: 220 alive / 147 gold
- SOCKS5: 238 alive / 155 gold

## Historical pool

- Discovered: 138957
- Ever alive: 23448
- Ever gold: 921

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
