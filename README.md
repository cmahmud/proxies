# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 420
- HTTP: 91 alive / 60 gold
- HTTPS: 66 alive / 26 gold
- SOCKS4: 188 alive / 164 gold
- SOCKS5: 188 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45503
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
