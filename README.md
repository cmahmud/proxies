# SyndProxy validated proxy pool

## Current pool

- Alive now: 552
- Gold now: 439
- HTTP: 121 alive / 82 gold
- HTTPS: 76 alive / 32 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 189 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44295
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
