# SyndProxy validated proxy pool

## Current pool

- Alive now: 620
- Gold now: 452
- HTTP: 130 alive / 83 gold
- HTTPS: 127 alive / 40 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 198 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44767
- Ever gold: 1413

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
