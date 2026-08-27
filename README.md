# SyndProxy validated proxy pool

## Current pool

- Alive now: 622
- Gold now: 400
- HTTP: 114 alive / 60 gold
- HTTPS: 143 alive / 14 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 188 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41327
- Ever gold: 1324

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
