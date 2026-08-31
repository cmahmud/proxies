# SyndProxy validated proxy pool

## Current pool

- Alive now: 602
- Gold now: 448
- HTTP: 120 alive / 84 gold
- HTTPS: 106 alive / 32 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 203 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45607
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
