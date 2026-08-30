# SyndProxy validated proxy pool

## Current pool

- Alive now: 610
- Gold now: 423
- HTTP: 128 alive / 81 gold
- HTTPS: 78 alive / 31 gold
- SOCKS4: 158 alive / 151 gold
- SOCKS5: 246 alive / 160 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43935
- Ever gold: 1379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
