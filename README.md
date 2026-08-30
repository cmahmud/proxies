# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 425
- HTTP: 109 alive / 73 gold
- HTTPS: 68 alive / 23 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 187 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44377
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
