# SyndProxy validated proxy pool

## Current pool

- Alive now: 542
- Gold now: 417
- HTTP: 90 alive / 59 gold
- HTTPS: 76 alive / 26 gold
- SOCKS4: 187 alive / 163 gold
- SOCKS5: 189 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45503
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
