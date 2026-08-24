# SyndProxy validated proxy pool

## Current pool

- Alive now: 601
- Gold now: 432
- HTTP: 127 alive / 77 gold
- HTTPS: 106 alive / 23 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 194 alive / 173 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34487
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
