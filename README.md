# SyndProxy validated proxy pool

## Current pool

- Alive now: 662
- Gold now: 404
- HTTP: 185 alive / 72 gold
- HTTPS: 83 alive / 14 gold
- SOCKS4: 189 alive / 156 gold
- SOCKS5: 205 alive / 162 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33302
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
