# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 426
- HTTP: 114 alive / 74 gold
- HTTPS: 70 alive / 26 gold
- SOCKS4: 165 alive / 161 gold
- SOCKS5: 189 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44370
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
