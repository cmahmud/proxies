# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 396
- HTTP: 121 alive / 74 gold
- HTTPS: 40 alive / 14 gold
- SOCKS4: 167 alive / 155 gold
- SOCKS5: 187 alive / 153 gold

## Historical pool

- Discovered: 176974
- Ever alive: 33276
- Ever gold: 1233

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
