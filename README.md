# SyndProxy validated proxy pool

## Current pool

- Alive now: 565
- Gold now: 419
- HTTP: 111 alive / 63 gold
- HTTPS: 90 alive / 25 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 195 alive / 171 gold

## Historical pool

- Discovered: 183874
- Ever alive: 35780
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
