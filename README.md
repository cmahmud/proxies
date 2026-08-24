# SyndProxy validated proxy pool

## Current pool

- Alive now: 569
- Gold now: 398
- HTTP: 142 alive / 62 gold
- HTTPS: 67 alive / 14 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 185 alive / 162 gold

## Historical pool

- Discovered: 179712
- Ever alive: 33508
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
