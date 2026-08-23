# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 390
- HTTP: 141 alive / 66 gold
- HTTPS: 40 alive / 14 gold
- SOCKS4: 175 alive / 151 gold
- SOCKS5: 194 alive / 159 gold

## Historical pool

- Discovered: 175458
- Ever alive: 33174
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
