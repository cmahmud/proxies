# SyndProxy validated proxy pool

## Current pool

- Alive now: 599
- Gold now: 454
- HTTP: 121 alive / 88 gold
- HTTPS: 113 alive / 33 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 195 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45612
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
