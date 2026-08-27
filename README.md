# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 389
- HTTP: 77 alive / 50 gold
- HTTPS: 54 alive / 15 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 180 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41631
- Ever gold: 1341

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
