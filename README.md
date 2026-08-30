# SyndProxy validated proxy pool

## Current pool

- Alive now: 602
- Gold now: 425
- HTTP: 130 alive / 82 gold
- HTTPS: 81 alive / 32 gold
- SOCKS4: 156 alive / 151 gold
- SOCKS5: 235 alive / 160 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43947
- Ever gold: 1381

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
