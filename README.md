# SyndProxy validated proxy pool

## Current pool

- Alive now: 607
- Gold now: 463
- HTTP: 127 alive / 95 gold
- HTTPS: 113 alive / 37 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 200 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44821
- Ever gold: 1414

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
