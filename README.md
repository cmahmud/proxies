# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 411
- HTTP: 104 alive / 57 gold
- HTTPS: 68 alive / 27 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 186 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45506
- Ever gold: 1435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
