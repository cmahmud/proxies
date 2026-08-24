# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 409
- HTTP: 105 alive / 72 gold
- HTTPS: 73 alive / 17 gold
- SOCKS4: 163 alive / 156 gold
- SOCKS5: 194 alive / 164 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33731
- Ever gold: 1249

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
