# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 429
- HTTP: 127 alive / 88 gold
- HTTPS: 79 alive / 30 gold
- SOCKS4: 159 alive / 152 gold
- SOCKS5: 176 alive / 159 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44084
- Ever gold: 1397

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
