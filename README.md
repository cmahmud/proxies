# SyndProxy validated proxy pool

## Current pool

- Alive now: 566
- Gold now: 411
- HTTP: 96 alive / 72 gold
- HTTPS: 121 alive / 17 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 182 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41915
- Ever gold: 1344

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
