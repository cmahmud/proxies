# SyndProxy validated proxy pool

## Current pool

- Alive now: 578
- Gold now: 417
- HTTP: 103 alive / 73 gold
- HTTPS: 124 alive / 21 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 179 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41979
- Ever gold: 1346

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
