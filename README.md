# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 412
- HTTP: 85 alive / 57 gold
- HTTPS: 50 alive / 24 gold
- SOCKS4: 174 alive / 163 gold
- SOCKS5: 178 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47099
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
