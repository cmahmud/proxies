# SyndProxy validated proxy pool

## Current pool

- Alive now: 612
- Gold now: 435
- HTTP: 142 alive / 80 gold
- HTTPS: 113 alive / 24 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 188 alive / 169 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34363
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
