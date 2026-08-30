# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 441
- HTTP: 119 alive / 85 gold
- HTTPS: 70 alive / 34 gold
- SOCKS4: 165 alive / 158 gold
- SOCKS5: 199 alive / 164 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44149
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
