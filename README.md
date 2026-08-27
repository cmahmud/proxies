# SyndProxy validated proxy pool

## Current pool

- Alive now: 647
- Gold now: 408
- HTTP: 115 alive / 66 gold
- HTTPS: 171 alive / 15 gold
- SOCKS4: 179 alive / 160 gold
- SOCKS5: 182 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40935
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
