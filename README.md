# SyndProxy validated proxy pool

## Current pool

- Alive now: 542
- Gold now: 412
- HTTP: 102 alive / 66 gold
- HTTPS: 74 alive / 17 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 191 alive / 168 gold

## Historical pool

- Discovered: 189543
- Ever alive: 39239
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
