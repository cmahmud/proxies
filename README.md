# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 430
- HTTP: 121 alive / 88 gold
- HTTPS: 86 alive / 33 gold
- SOCKS4: 162 alive / 150 gold
- SOCKS5: 180 alive / 159 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44074
- Ever gold: 1394

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
