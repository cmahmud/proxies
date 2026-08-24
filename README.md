# SyndProxy validated proxy pool

## Current pool

- Alive now: 599
- Gold now: 434
- HTTP: 133 alive / 79 gold
- HTTPS: 99 alive / 23 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 193 alive / 172 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34480
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
