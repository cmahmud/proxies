# SyndProxy validated proxy pool

## Current pool

- Alive now: 582
- Gold now: 454
- HTTP: 122 alive / 88 gold
- HTTPS: 99 alive / 34 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 191 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45650
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
