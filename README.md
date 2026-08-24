# SyndProxy validated proxy pool

## Current pool

- Alive now: 572
- Gold now: 429
- HTTP: 136 alive / 77 gold
- HTTPS: 76 alive / 21 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 188 alive / 169 gold

## Historical pool

- Discovered: 181482
- Ever alive: 33911
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
