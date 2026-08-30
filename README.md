# SyndProxy validated proxy pool

## Current pool

- Alive now: 579
- Gold now: 439
- HTTP: 114 alive / 77 gold
- HTTPS: 103 alive / 33 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 194 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44630
- Ever gold: 1408

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
