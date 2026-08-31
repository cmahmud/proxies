# SyndProxy validated proxy pool

## Current pool

- Alive now: 606
- Gold now: 443
- HTTP: 118 alive / 80 gold
- HTTPS: 112 alive / 30 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 197 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45639
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
