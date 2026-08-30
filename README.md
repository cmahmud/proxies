# SyndProxy validated proxy pool

## Current pool

- Alive now: 611
- Gold now: 453
- HTTP: 128 alive / 83 gold
- HTTPS: 122 alive / 40 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 195 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44764
- Ever gold: 1413

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
