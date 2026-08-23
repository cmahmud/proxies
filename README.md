# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 350
- HTTP: 110 alive / 33 gold
- HTTPS: 37 alive / 8 gold
- SOCKS4: 180 alive / 153 gold
- SOCKS5: 198 alive / 156 gold

## Historical pool

- Discovered: 172299
- Ever alive: 32953
- Ever gold: 1217

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
