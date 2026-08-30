# SyndProxy validated proxy pool

## Current pool

- Alive now: 621
- Gold now: 468
- HTTP: 137 alive / 93 gold
- HTTPS: 116 alive / 40 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 195 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44863
- Ever gold: 1417

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
