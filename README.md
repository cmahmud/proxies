# SyndProxy validated proxy pool

## Current pool

- Alive now: 634
- Gold now: 400
- HTTP: 119 alive / 59 gold
- HTTPS: 151 alive / 15 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 187 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41325
- Ever gold: 1324

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
