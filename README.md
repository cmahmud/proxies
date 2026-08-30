# SyndProxy validated proxy pool

## Current pool

- Alive now: 636
- Gold now: 454
- HTTP: 132 alive / 84 gold
- HTTPS: 138 alive / 39 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 198 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44747
- Ever gold: 1413

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
