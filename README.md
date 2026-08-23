# SyndProxy validated proxy pool

## Current pool

- Alive now: 477
- Gold now: 376
- HTTP: 81 alive / 48 gold
- HTTPS: 45 alive / 12 gold
- SOCKS4: 168 alive / 156 gold
- SOCKS5: 183 alive / 160 gold

## Historical pool

- Discovered: 172309
- Ever alive: 32970
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
