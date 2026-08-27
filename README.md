# SyndProxy validated proxy pool

## Current pool

- Alive now: 665
- Gold now: 405
- HTTP: 134 alive / 69 gold
- HTTPS: 161 alive / 14 gold
- SOCKS4: 176 alive / 156 gold
- SOCKS5: 194 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40533
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
