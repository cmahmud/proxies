# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 381
- HTTP: 134 alive / 62 gold
- HTTPS: 40 alive / 15 gold
- SOCKS4: 171 alive / 152 gold
- SOCKS5: 173 alive / 152 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33210
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
