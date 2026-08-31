# SyndProxy validated proxy pool

## Current pool

- Alive now: 655
- Gold now: 478
- HTTP: 145 alive / 98 gold
- HTTPS: 126 alive / 41 gold
- SOCKS4: 182 alive / 164 gold
- SOCKS5: 202 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45104
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
