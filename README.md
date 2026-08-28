# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 408
- HTTP: 112 alive / 75 gold
- HTTPS: 85 alive / 17 gold
- SOCKS4: 160 alive / 156 gold
- SOCKS5: 172 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43087
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
