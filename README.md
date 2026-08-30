# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 446
- HTTP: 110 alive / 81 gold
- HTTPS: 73 alive / 34 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 206 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44587
- Ever gold: 1407

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
