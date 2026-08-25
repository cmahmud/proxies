# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 416
- HTTP: 95 alive / 62 gold
- HTTPS: 74 alive / 20 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 188 alive / 172 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35598
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
