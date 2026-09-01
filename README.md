# SyndProxy validated proxy pool

## Current pool

- Alive now: 460
- Gold now: 406
- HTTP: 75 alive / 52 gold
- HTTPS: 37 alive / 21 gold
- SOCKS4: 171 alive / 163 gold
- SOCKS5: 177 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47108
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
