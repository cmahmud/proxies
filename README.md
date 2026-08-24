# SyndProxy validated proxy pool

## Current pool

- Alive now: 569
- Gold now: 380
- HTTP: 115 alive / 63 gold
- HTTPS: 110 alive / 15 gold
- SOCKS4: 175 alive / 152 gold
- SOCKS5: 169 alive / 150 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33217
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
