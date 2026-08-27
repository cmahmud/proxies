# SyndProxy validated proxy pool

## Current pool

- Alive now: 623
- Gold now: 408
- HTTP: 113 alive / 64 gold
- HTTPS: 161 alive / 18 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 178 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40891
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
