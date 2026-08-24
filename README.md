# SyndProxy validated proxy pool

## Current pool

- Alive now: 591
- Gold now: 438
- HTTP: 131 alive / 86 gold
- HTTPS: 96 alive / 20 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 190 alive / 171 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34424
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
