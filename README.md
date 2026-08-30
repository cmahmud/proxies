# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 421
- HTTP: 126 alive / 82 gold
- HTTPS: 69 alive / 28 gold
- SOCKS4: 160 alive / 151 gold
- SOCKS5: 190 alive / 160 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44061
- Ever gold: 1394

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
