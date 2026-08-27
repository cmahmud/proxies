# SyndProxy validated proxy pool

## Current pool

- Alive now: 660
- Gold now: 409
- HTTP: 101 alive / 65 gold
- HTTPS: 188 alive / 15 gold
- SOCKS4: 179 alive / 159 gold
- SOCKS5: 192 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40691
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
