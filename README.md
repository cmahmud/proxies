# SyndProxy validated proxy pool

## Current pool

- Alive now: 614
- Gold now: 407
- HTTP: 108 alive / 62 gold
- HTTPS: 157 alive / 18 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 177 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40892
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
