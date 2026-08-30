# SyndProxy validated proxy pool

## Current pool

- Alive now: 582
- Gold now: 452
- HTTP: 141 alive / 92 gold
- HTTPS: 78 alive / 36 gold
- SOCKS4: 164 alive / 158 gold
- SOCKS5: 199 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44179
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
