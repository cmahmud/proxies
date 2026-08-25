# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 418
- HTTP: 93 alive / 63 gold
- HTTPS: 71 alive / 19 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 188 alive / 174 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35602
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
