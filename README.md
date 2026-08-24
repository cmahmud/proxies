# SyndProxy validated proxy pool

## Current pool

- Alive now: 598
- Gold now: 401
- HTTP: 171 alive / 72 gold
- HTTPS: 64 alive / 15 gold
- SOCKS4: 175 alive / 154 gold
- SOCKS5: 188 alive / 160 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33285
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
