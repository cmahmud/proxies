# SyndProxy validated proxy pool

## Current pool

- Alive now: 670
- Gold now: 478
- HTTP: 160 alive / 99 gold
- HTTPS: 137 alive / 43 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 205 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44970
- Ever gold: 1421

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
