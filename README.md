# SyndProxy validated proxy pool

## Current pool

- Alive now: 713
- Gold now: 470
- HTTP: 180 alive / 93 gold
- HTTPS: 130 alive / 38 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 236 alive / 178 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45285
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
