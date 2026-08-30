# SyndProxy validated proxy pool

## Current pool

- Alive now: 602
- Gold now: 443
- HTTP: 110 alive / 77 gold
- HTTPS: 131 alive / 35 gold
- SOCKS4: 166 alive / 158 gold
- SOCKS5: 195 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44658
- Ever gold: 1409

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
