# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 411
- HTTP: 110 alive / 73 gold
- HTTPS: 64 alive / 18 gold
- SOCKS4: 167 alive / 156 gold
- SOCKS5: 185 alive / 164 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33723
- Ever gold: 1249

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
