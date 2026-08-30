# SyndProxy validated proxy pool

## Current pool

- Alive now: 572
- Gold now: 445
- HTTP: 133 alive / 92 gold
- HTTPS: 70 alive / 33 gold
- SOCKS4: 165 alive / 158 gold
- SOCKS5: 204 alive / 162 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44248
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
