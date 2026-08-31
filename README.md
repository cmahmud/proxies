# SyndProxy validated proxy pool

## Current pool

- Alive now: 694
- Gold now: 457
- HTTP: 161 alive / 90 gold
- HTTPS: 135 alive / 32 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 224 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45314
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
