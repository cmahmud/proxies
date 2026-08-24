# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 373
- HTTP: 118 alive / 65 gold
- HTTPS: 78 alive / 15 gold
- SOCKS4: 165 alive / 147 gold
- SOCKS5: 177 alive / 146 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33218
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
