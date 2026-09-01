# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 429
- HTTP: 104 alive / 75 gold
- HTTPS: 74 alive / 26 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 181 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47051
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
