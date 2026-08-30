# SyndProxy validated proxy pool

## Current pool

- Alive now: 598
- Gold now: 425
- HTTP: 128 alive / 83 gold
- HTTPS: 79 alive / 31 gold
- SOCKS4: 156 alive / 151 gold
- SOCKS5: 235 alive / 160 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43943
- Ever gold: 1381

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
