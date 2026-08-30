# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 424
- HTTP: 120 alive / 72 gold
- HTTPS: 65 alive / 23 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 185 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44392
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
