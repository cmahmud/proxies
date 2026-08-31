# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 418
- HTTP: 91 alive / 58 gold
- HTTPS: 66 alive / 28 gold
- SOCKS4: 187 alive / 163 gold
- SOCKS5: 189 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45503
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
