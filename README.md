# SyndProxy validated proxy pool

## Current pool

- Alive now: 598
- Gold now: 437
- HTTP: 132 alive / 80 gold
- HTTPS: 107 alive / 25 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 190 alive / 170 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34344
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
