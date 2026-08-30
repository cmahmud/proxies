# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 431
- HTTP: 115 alive / 86 gold
- HTTPS: 72 alive / 35 gold
- SOCKS4: 157 alive / 152 gold
- SOCKS5: 175 alive / 158 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44089
- Ever gold: 1397

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
