# SyndProxy validated proxy pool

## Current pool

- Alive now: 601
- Gold now: 441
- HTTP: 116 alive / 79 gold
- HTTPS: 112 alive / 29 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 196 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45639
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
