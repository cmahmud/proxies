# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 440
- HTTP: 113 alive / 81 gold
- HTTPS: 59 alive / 28 gold
- SOCKS4: 165 alive / 160 gold
- SOCKS5: 200 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44572
- Ever gold: 1406

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
