# SyndProxy validated proxy pool

## Current pool

- Alive now: 607
- Gold now: 435
- HTTP: 136 alive / 80 gold
- HTTPS: 117 alive / 24 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 185 alive / 169 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34359
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
