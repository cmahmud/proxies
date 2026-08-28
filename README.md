# SyndProxy validated proxy pool

## Current pool

- Alive now: 542
- Gold now: 407
- HTTP: 88 alive / 63 gold
- HTTPS: 99 alive / 20 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 179 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42989
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
