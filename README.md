# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 383
- HTTP: 142 alive / 61 gold
- HTTPS: 47 alive / 16 gold
- SOCKS4: 168 alive / 154 gold
- SOCKS5: 172 alive / 152 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33210
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
