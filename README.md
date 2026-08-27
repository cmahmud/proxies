# SyndProxy validated proxy pool

## Current pool

- Alive now: 648
- Gold now: 426
- HTTP: 117 alive / 80 gold
- HTTPS: 155 alive / 19 gold
- SOCKS4: 180 alive / 159 gold
- SOCKS5: 196 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42175
- Ever gold: 1353

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
