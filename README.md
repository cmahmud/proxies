# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 439
- HTTP: 92 alive / 69 gold
- HTTPS: 97 alive / 30 gold
- SOCKS4: 172 alive / 163 gold
- SOCKS5: 188 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47458
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
