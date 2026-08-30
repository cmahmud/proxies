# SyndProxy validated proxy pool

## Current pool

- Alive now: 641
- Gold now: 485
- HTTP: 149 alive / 102 gold
- HTTPS: 117 alive / 45 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 204 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44980
- Ever gold: 1421

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
