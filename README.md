# SyndProxy validated proxy pool

## Current pool

- Alive now: 674
- Gold now: 485
- HTTP: 163 alive / 103 gold
- HTTPS: 143 alive / 43 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 198 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45238
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
