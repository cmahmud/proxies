# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 419
- HTTP: 86 alive / 60 gold
- HTTPS: 73 alive / 28 gold
- SOCKS4: 189 alive / 163 gold
- SOCKS5: 191 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45503
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
