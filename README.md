# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 436
- HTTP: 123 alive / 90 gold
- HTTPS: 68 alive / 35 gold
- SOCKS4: 158 alive / 152 gold
- SOCKS5: 175 alive / 159 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44090
- Ever gold: 1397

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
