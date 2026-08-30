# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 424
- HTTP: 110 alive / 71 gold
- HTTPS: 62 alive / 28 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 187 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44362
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
