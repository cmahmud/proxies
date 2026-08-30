# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 419
- HTTP: 119 alive / 70 gold
- HTTPS: 66 alive / 22 gold
- SOCKS4: 164 alive / 161 gold
- SOCKS5: 180 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44387
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
