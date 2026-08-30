# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 441
- HTTP: 114 alive / 85 gold
- HTTPS: 67 alive / 34 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 184 alive / 164 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44095
- Ever gold: 1397

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
