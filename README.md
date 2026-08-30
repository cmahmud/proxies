# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 446
- HTTP: 116 alive / 82 gold
- HTTPS: 73 alive / 34 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 193 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44601
- Ever gold: 1408

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
