# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 398
- HTTP: 85 alive / 54 gold
- HTTPS: 64 alive / 18 gold
- SOCKS4: 177 alive / 164 gold
- SOCKS5: 182 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41607
- Ever gold: 1341

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
