# SyndProxy validated proxy pool

## Current pool

- Alive now: 657
- Gold now: 408
- HTTP: 101 alive / 65 gold
- HTTPS: 185 alive / 14 gold
- SOCKS4: 178 alive / 159 gold
- SOCKS5: 193 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40693
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
