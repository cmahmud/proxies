# SyndProxy validated proxy pool

## Current pool

- Alive now: 572
- Gold now: 442
- HTTP: 95 alive / 72 gold
- HTTPS: 117 alive / 31 gold
- SOCKS4: 174 alive / 163 gold
- SOCKS5: 186 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47449
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
