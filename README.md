# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 383
- HTTP: 127 alive / 70 gold
- HTTPS: 95 alive / 14 gold
- SOCKS4: 165 alive / 149 gold
- SOCKS5: 187 alive / 150 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33234
- Ever gold: 1231

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
