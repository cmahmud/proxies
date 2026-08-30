# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 448
- HTTP: 113 alive / 83 gold
- HTTPS: 67 alive / 32 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 209 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44588
- Ever gold: 1407

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
