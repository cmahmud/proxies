# SyndProxy validated proxy pool

## Current pool

- Alive now: 640
- Gold now: 442
- HTTP: 142 alive / 77 gold
- HTTPS: 126 alive / 27 gold
- SOCKS4: 184 alive / 165 gold
- SOCKS5: 188 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47620
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
