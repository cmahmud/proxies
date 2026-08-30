# SyndProxy validated proxy pool

## Current pool

- Alive now: 559
- Gold now: 417
- HTTP: 119 alive / 79 gold
- HTTPS: 88 alive / 27 gold
- SOCKS4: 162 alive / 151 gold
- SOCKS5: 190 alive / 160 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44041
- Ever gold: 1392

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
