# SyndProxy validated proxy pool

## Current pool

- Alive now: 612
- Gold now: 453
- HTTP: 127 alive / 83 gold
- HTTPS: 123 alive / 40 gold
- SOCKS4: 165 alive / 160 gold
- SOCKS5: 197 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44765
- Ever gold: 1413

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
