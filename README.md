# SyndProxy validated proxy pool

## Current pool

- Alive now: 476
- Gold now: 377
- HTTP: 82 alive / 47 gold
- HTTPS: 36 alive / 12 gold
- SOCKS4: 175 alive / 156 gold
- SOCKS5: 183 alive / 162 gold

## Historical pool

- Discovered: 172315
- Ever alive: 32972
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
