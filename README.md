# SyndProxy validated proxy pool

## Current pool

- Alive now: 485
- Gold now: 395
- HTTP: 105 alive / 74 gold
- HTTPS: 40 alive / 18 gold
- SOCKS4: 167 alive / 150 gold
- SOCKS5: 173 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48192
- Ever gold: 1522

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
