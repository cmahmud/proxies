# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 423
- HTTP: 116 alive / 75 gold
- HTTPS: 55 alive / 20 gold
- SOCKS4: 165 alive / 160 gold
- SOCKS5: 195 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44510
- Ever gold: 1403

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
