# SyndProxy validated proxy pool

## Current pool

- Alive now: 609
- Gold now: 460
- HTTP: 133 alive / 91 gold
- HTTPS: 114 alive / 38 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 197 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44815
- Ever gold: 1414

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
