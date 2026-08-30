# SyndProxy validated proxy pool

## Current pool

- Alive now: 612
- Gold now: 459
- HTTP: 132 alive / 91 gold
- HTTPS: 116 alive / 37 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 197 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44814
- Ever gold: 1414

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
