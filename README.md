# SyndProxy validated proxy pool

## Current pool

- Alive now: 486
- Gold now: 381
- HTTP: 87 alive / 57 gold
- HTTPS: 54 alive / 11 gold
- SOCKS4: 165 alive / 155 gold
- SOCKS5: 180 alive / 158 gold

## Historical pool

- Discovered: 174835
- Ever alive: 33117
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
