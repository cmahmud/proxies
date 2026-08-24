# SyndProxy validated proxy pool

## Current pool

- Alive now: 595
- Gold now: 401
- HTTP: 166 alive / 71 gold
- HTTPS: 70 alive / 16 gold
- SOCKS4: 173 alive / 154 gold
- SOCKS5: 186 alive / 160 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33285
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
