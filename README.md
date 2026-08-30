# SyndProxy validated proxy pool

## Current pool

- Alive now: 590
- Gold now: 458
- HTTP: 125 alive / 90 gold
- HTTPS: 105 alive / 34 gold
- SOCKS4: 162 alive / 160 gold
- SOCKS5: 198 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44794
- Ever gold: 1414

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
