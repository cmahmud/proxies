# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 421
- HTTP: 111 alive / 68 gold
- HTTPS: 66 alive / 24 gold
- SOCKS4: 164 alive / 162 gold
- SOCKS5: 190 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44379
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
