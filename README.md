# SyndProxy validated proxy pool

## Current pool

- Alive now: 619
- Gold now: 458
- HTTP: 130 alive / 91 gold
- HTTPS: 124 alive / 36 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 195 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44810
- Ever gold: 1414

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
