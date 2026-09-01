# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 420
- HTTP: 89 alive / 67 gold
- HTTPS: 106 alive / 28 gold
- SOCKS4: 171 alive / 157 gold
- SOCKS5: 174 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47267
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
