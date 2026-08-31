# SyndProxy validated proxy pool

## Current pool

- Alive now: 577
- Gold now: 448
- HTTP: 120 alive / 84 gold
- HTTPS: 80 alive / 32 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 204 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45567
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
