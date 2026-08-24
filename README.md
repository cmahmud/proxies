# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 386
- HTTP: 116 alive / 55 gold
- HTTPS: 67 alive / 14 gold
- SOCKS4: 168 alive / 155 gold
- SOCKS5: 192 alive / 162 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33380
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
