# SyndProxy validated proxy pool

## Current pool

- Alive now: 604
- Gold now: 447
- HTTP: 120 alive / 82 gold
- HTTPS: 109 alive / 32 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 198 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45639
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
