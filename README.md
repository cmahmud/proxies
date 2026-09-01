# SyndProxy validated proxy pool

## Current pool

- Alive now: 600
- Gold now: 454
- HTTP: 126 alive / 87 gold
- HTTPS: 113 alive / 29 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 190 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46730
- Ever gold: 1447

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
