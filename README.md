# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 417
- HTTP: 102 alive / 73 gold
- HTTPS: 120 alive / 21 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 179 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41980
- Ever gold: 1346

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
