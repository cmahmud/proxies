# SyndProxy validated proxy pool

## Current pool

- Alive now: 599
- Gold now: 456
- HTTP: 124 alive / 87 gold
- HTTPS: 112 alive / 28 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 192 alive / 180 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46730
- Ever gold: 1447

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
