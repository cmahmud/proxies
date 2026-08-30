# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 443
- HTTP: 124 alive / 81 gold
- HTTPS: 63 alive / 32 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 198 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44583
- Ever gold: 1407

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
