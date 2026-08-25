# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 416
- HTTP: 115 alive / 71 gold
- HTTPS: 89 alive / 20 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 197 alive / 165 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35229
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
