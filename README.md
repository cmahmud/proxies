# SyndProxy validated proxy pool

## Current pool

- Alive now: 624
- Gold now: 459
- HTTP: 134 alive / 95 gold
- HTTPS: 122 alive / 36 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 200 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44831
- Ever gold: 1414

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
