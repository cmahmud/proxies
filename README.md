# SyndProxy validated proxy pool

## Current pool

- Alive now: 707
- Gold now: 468
- HTTP: 175 alive / 93 gold
- HTTPS: 129 alive / 36 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 231 alive / 180 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45285
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
