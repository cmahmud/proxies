# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 417
- HTTP: 91 alive / 66 gold
- HTTPS: 63 alive / 23 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 186 alive / 166 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47072
- Ever gold: 1464

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
