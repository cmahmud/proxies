# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 416
- HTTP: 87 alive / 58 gold
- HTTPS: 76 alive / 26 gold
- SOCKS4: 188 alive / 163 gold
- SOCKS5: 192 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45503
- Ever gold: 1435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
