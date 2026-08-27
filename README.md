# SyndProxy validated proxy pool

## Current pool

- Alive now: 542
- Gold now: 421
- HTTP: 102 alive / 75 gold
- HTTPS: 99 alive / 24 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 174 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41785
- Ever gold: 1343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
