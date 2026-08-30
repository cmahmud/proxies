# SyndProxy validated proxy pool

## Current pool

- Alive now: 612
- Gold now: 452
- HTTP: 130 alive / 82 gold
- HTTPS: 123 alive / 39 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 193 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44760
- Ever gold: 1413

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
