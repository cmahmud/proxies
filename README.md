# SyndProxy validated proxy pool

## Current pool

- Alive now: 616
- Gold now: 418
- HTTP: 108 alive / 66 gold
- HTTPS: 147 alive / 24 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 186 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41300
- Ever gold: 1324

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
