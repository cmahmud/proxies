# SyndProxy validated proxy pool

## Current pool

- Alive now: 660
- Gold now: 418
- HTTP: 126 alive / 72 gold
- HTTPS: 173 alive / 22 gold
- SOCKS4: 173 alive / 157 gold
- SOCKS5: 188 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40485
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
