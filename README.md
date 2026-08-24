# SyndProxy validated proxy pool

## Current pool

- Alive now: 592
- Gold now: 437
- HTTP: 127 alive / 80 gold
- HTTPS: 105 alive / 24 gold
- SOCKS4: 168 alive / 162 gold
- SOCKS5: 192 alive / 171 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34335
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
