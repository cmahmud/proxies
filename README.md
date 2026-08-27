# SyndProxy validated proxy pool

## Current pool

- Alive now: 628
- Gold now: 418
- HTTP: 108 alive / 69 gold
- HTTPS: 162 alive / 20 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 181 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40966
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
