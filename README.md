# SyndProxy validated proxy pool

## Current pool

- Alive now: 608
- Gold now: 436
- HTTP: 137 alive / 84 gold
- HTTPS: 103 alive / 19 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 191 alive / 171 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34439
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
