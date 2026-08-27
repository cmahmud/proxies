# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 409
- HTTP: 107 alive / 68 gold
- HTTPS: 118 alive / 18 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 177 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41907
- Ever gold: 1344

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
