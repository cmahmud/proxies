# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 436
- HTTP: 106 alive / 75 gold
- HTTPS: 50 alive / 26 gold
- SOCKS4: 199 alive / 170 gold
- SOCKS5: 183 alive / 165 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49111
- Ever gold: 1573

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
