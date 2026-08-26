# SyndProxy validated proxy pool

## Current pool

- Alive now: 636
- Gold now: 408
- HTTP: 134 alive / 72 gold
- HTTPS: 156 alive / 21 gold
- SOCKS4: 168 alive / 152 gold
- SOCKS5: 178 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40376
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
