# SyndProxy validated proxy pool

## Current pool

- Alive now: 650
- Gold now: 382
- HTTP: 136 alive / 66 gold
- HTTPS: 168 alive / 20 gold
- SOCKS4: 167 alive / 146 gold
- SOCKS5: 179 alive / 150 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39715
- Ever gold: 1301

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
