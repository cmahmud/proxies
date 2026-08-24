# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 384
- HTTP: 113 alive / 59 gold
- HTTPS: 44 alive / 8 gold
- SOCKS4: 167 alive / 155 gold
- SOCKS5: 177 alive / 162 gold

## Historical pool

- Discovered: 179062
- Ever alive: 33442
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
