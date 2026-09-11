# SyndProxy validated proxy pool

## Current pool

- Alive now: 408
- Gold now: 349
- HTTP: 97 alive / 72 gold
- HTTPS: 46 alive / 20 gold
- SOCKS4: 89 alive / 86 gold
- SOCKS5: 176 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48686
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
