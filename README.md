# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 421
- HTTP: 116 alive / 70 gold
- HTTPS: 58 alive / 24 gold
- SOCKS4: 164 alive / 160 gold
- SOCKS5: 194 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44465
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
