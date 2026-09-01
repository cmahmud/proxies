# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 429
- HTTP: 95 alive / 71 gold
- HTTPS: 64 alive / 28 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 183 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47030
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
