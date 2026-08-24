# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 391
- HTTP: 94 alive / 48 gold
- HTTPS: 45 alive / 14 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 187 alive / 167 gold

## Historical pool

- Discovered: 180270
- Ever alive: 33548
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
