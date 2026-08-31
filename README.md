# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 412
- HTTP: 90 alive / 57 gold
- HTTPS: 70 alive / 24 gold
- SOCKS4: 188 alive / 162 gold
- SOCKS5: 191 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45503
- Ever gold: 1435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
