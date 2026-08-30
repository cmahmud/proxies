# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 428
- HTTP: 116 alive / 81 gold
- HTTPS: 63 alive / 24 gold
- SOCKS4: 164 alive / 158 gold
- SOCKS5: 205 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44336
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
