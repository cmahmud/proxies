# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 394
- HTTP: 102 alive / 59 gold
- HTTPS: 67 alive / 14 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 176 alive / 163 gold

## Historical pool

- Discovered: 179712
- Ever alive: 33508
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
