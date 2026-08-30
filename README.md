# SyndProxy validated proxy pool

## Current pool

- Alive now: 597
- Gold now: 457
- HTTP: 124 alive / 90 gold
- HTTPS: 110 alive / 34 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 197 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44800
- Ever gold: 1414

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
