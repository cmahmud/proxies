# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 439
- HTTP: 121 alive / 90 gold
- HTTPS: 67 alive / 36 gold
- SOCKS4: 154 alive / 152 gold
- SOCKS5: 178 alive / 161 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44086
- Ever gold: 1397

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
