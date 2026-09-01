# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 417
- HTTP: 83 alive / 66 gold
- HTTPS: 101 alive / 24 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 185 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47174
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
