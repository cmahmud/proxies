# SyndProxy validated proxy pool

## Current pool

- Alive now: 596
- Gold now: 457
- HTTP: 118 alive / 85 gold
- HTTPS: 115 alive / 37 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 190 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45627
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
