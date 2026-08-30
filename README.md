# SyndProxy validated proxy pool

## Current pool

- Alive now: 667
- Gold now: 478
- HTTP: 159 alive / 98 gold
- HTTPS: 136 alive / 44 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 204 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44969
- Ever gold: 1421

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
