# SyndProxy validated proxy pool

## Current pool

- Alive now: 606
- Gold now: 454
- HTTP: 124 alive / 85 gold
- HTTPS: 118 alive / 35 gold
- SOCKS4: 175 alive / 163 gold
- SOCKS5: 189 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45619
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
