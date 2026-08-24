# SyndProxy validated proxy pool

## Current pool

- Alive now: 612
- Gold now: 436
- HTTP: 144 alive / 82 gold
- HTTPS: 94 alive / 21 gold
- SOCKS4: 182 alive / 162 gold
- SOCKS5: 192 alive / 171 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34448
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
