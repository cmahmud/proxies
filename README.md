# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 383
- HTTP: 122 alive / 65 gold
- HTTPS: 89 alive / 15 gold
- SOCKS4: 169 alive / 152 gold
- SOCKS5: 178 alive / 151 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33218
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
