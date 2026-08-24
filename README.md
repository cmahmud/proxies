# SyndProxy validated proxy pool

## Current pool

- Alive now: 610
- Gold now: 434
- HTTP: 134 alive / 79 gold
- HTTPS: 121 alive / 24 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 185 alive / 169 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34359
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
