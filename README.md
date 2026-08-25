# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 416
- HTTP: 94 alive / 64 gold
- HTTPS: 90 alive / 22 gold
- SOCKS4: 165 alive / 160 gold
- SOCKS5: 187 alive / 170 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35636
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
