# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 442
- HTTP: 93 alive / 73 gold
- HTTPS: 118 alive / 31 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 187 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47449
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
