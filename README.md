# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 417
- HTTP: 78 alive / 63 gold
- HTTPS: 48 alive / 19 gold
- SOCKS4: 192 alive / 163 gold
- SOCKS5: 183 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47120
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
