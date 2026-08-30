# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 440
- HTTP: 123 alive / 84 gold
- HTTPS: 70 alive / 36 gold
- SOCKS4: 170 alive / 158 gold
- SOCKS5: 190 alive / 162 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44112
- Ever gold: 1397

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
