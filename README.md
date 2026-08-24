# SyndProxy validated proxy pool

## Current pool

- Alive now: 607
- Gold now: 434
- HTTP: 127 alive / 79 gold
- HTTPS: 106 alive / 23 gold
- SOCKS4: 183 alive / 162 gold
- SOCKS5: 191 alive / 170 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34467
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
