# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 390
- HTTP: 96 alive / 54 gold
- HTTPS: 51 alive / 12 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 178 alive / 164 gold

## Historical pool

- Discovered: 180270
- Ever alive: 33552
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
