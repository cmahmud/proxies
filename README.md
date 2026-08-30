# SyndProxy validated proxy pool

## Current pool

- Alive now: 581
- Gold now: 439
- HTTP: 114 alive / 76 gold
- HTTPS: 103 alive / 34 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 198 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44618
- Ever gold: 1408

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
