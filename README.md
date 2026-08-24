# SyndProxy validated proxy pool

## Current pool

- Alive now: 592
- Gold now: 439
- HTTP: 123 alive / 81 gold
- HTTPS: 111 alive / 24 gold
- SOCKS4: 168 alive / 162 gold
- SOCKS5: 190 alive / 172 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34332
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
