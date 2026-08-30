# SyndProxy validated proxy pool

## Current pool

- Alive now: 606
- Gold now: 452
- HTTP: 127 alive / 83 gold
- HTTPS: 115 alive / 40 gold
- SOCKS4: 163 alive / 159 gold
- SOCKS5: 201 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44768
- Ever gold: 1413

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
