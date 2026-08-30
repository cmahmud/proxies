# SyndProxy validated proxy pool

## Current pool

- Alive now: 590
- Gold now: 446
- HTTP: 116 alive / 81 gold
- HTTPS: 113 alive / 34 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 196 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44646
- Ever gold: 1409

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
