# SyndProxy validated proxy pool

## Current pool

- Alive now: 592
- Gold now: 451
- HTTP: 131 alive / 84 gold
- HTTPS: 90 alive / 34 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 196 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45602
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
