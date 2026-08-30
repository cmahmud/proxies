# SyndProxy validated proxy pool

## Current pool

- Alive now: 618
- Gold now: 467
- HTTP: 134 alive / 95 gold
- HTTPS: 112 alive / 38 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 204 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44850
- Ever gold: 1416

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
