# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 410
- HTTP: 102 alive / 56 gold
- HTTPS: 67 alive / 27 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 187 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45506
- Ever gold: 1435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
