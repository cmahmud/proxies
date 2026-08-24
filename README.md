# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 416
- HTTP: 104 alive / 75 gold
- HTTPS: 75 alive / 18 gold
- SOCKS4: 162 alive / 158 gold
- SOCKS5: 190 alive / 165 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33733
- Ever gold: 1249

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
