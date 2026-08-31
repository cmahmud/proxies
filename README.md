# SyndProxy validated proxy pool

## Current pool

- Alive now: 564
- Gold now: 421
- HTTP: 108 alive / 66 gold
- HTTPS: 69 alive / 23 gold
- SOCKS4: 186 alive / 161 gold
- SOCKS5: 201 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45524
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
