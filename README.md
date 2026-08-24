# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 410
- HTTP: 105 alive / 73 gold
- HTTPS: 77 alive / 17 gold
- SOCKS4: 165 alive / 156 gold
- SOCKS5: 196 alive / 164 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33731
- Ever gold: 1249

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
