# SyndProxy validated proxy pool

## Current pool

- Alive now: 595
- Gold now: 456
- HTTP: 123 alive / 90 gold
- HTTPS: 112 alive / 34 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 195 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44802
- Ever gold: 1414

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
