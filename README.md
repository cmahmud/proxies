# SyndProxy validated proxy pool

## Current pool

- Alive now: 605
- Gold now: 453
- HTTP: 125 alive / 83 gold
- HTTPS: 120 alive / 39 gold
- SOCKS4: 165 alive / 160 gold
- SOCKS5: 195 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44752
- Ever gold: 1413

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
