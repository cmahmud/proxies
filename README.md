# SyndProxy validated proxy pool

## Current pool

- Alive now: 606
- Gold now: 452
- HTTP: 125 alive / 84 gold
- HTTPS: 118 alive / 34 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 190 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45619
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
