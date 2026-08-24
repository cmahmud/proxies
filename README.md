# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 379
- HTTP: 127 alive / 68 gold
- HTTPS: 56 alive / 13 gold
- SOCKS4: 163 alive / 151 gold
- SOCKS5: 177 alive / 147 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33229
- Ever gold: 1231

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
