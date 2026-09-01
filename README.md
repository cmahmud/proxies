# SyndProxy validated proxy pool

## Current pool

- Alive now: 653
- Gold now: 467
- HTTP: 138 alive / 95 gold
- HTTPS: 139 alive / 36 gold
- SOCKS4: 182 alive / 164 gold
- SOCKS5: 194 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46921
- Ever gold: 1457

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
