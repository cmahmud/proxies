# SyndProxy validated proxy pool

## Current pool

- Alive now: 616
- Gold now: 435
- HTTP: 130 alive / 80 gold
- HTTPS: 106 alive / 22 gold
- SOCKS4: 186 alive / 162 gold
- SOCKS5: 194 alive / 171 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34464
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
