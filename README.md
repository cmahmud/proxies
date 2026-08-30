# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 425
- HTTP: 115 alive / 75 gold
- HTTPS: 68 alive / 25 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 194 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44340
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
