# SyndProxy private pool

## Current pool

- Alive now: 1028
- Gold now: 255
- HTTP: 409 alive / 29 gold
- HTTPS: 186 alive / 5 gold
- SOCKS4: 212 alive / 117 gold
- SOCKS5: 221 alive / 104 gold

## Historical pool

- Discovered: 99106
- Ever alive: 11776
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
