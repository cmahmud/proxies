# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 387
- HTTP: 105 alive / 61 gold
- HTTPS: 41 alive / 11 gold
- SOCKS4: 177 alive / 157 gold
- SOCKS5: 188 alive / 158 gold

## Historical pool

- Discovered: 174803
- Ever alive: 33089
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
