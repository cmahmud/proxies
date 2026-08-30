# SyndProxy validated proxy pool

## Current pool

- Alive now: 632
- Gold now: 477
- HTTP: 144 alive / 98 gold
- HTTPS: 113 alive / 41 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 204 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44927
- Ever gold: 1419

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
