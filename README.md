# SyndProxy validated proxy pool

## Current pool

- Alive now: 570
- Gold now: 380
- HTTP: 120 alive / 62 gold
- HTTPS: 110 alive / 15 gold
- SOCKS4: 175 alive / 152 gold
- SOCKS5: 165 alive / 151 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33217
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
