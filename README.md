# SyndProxy validated proxy pool

## Current pool

- Alive now: 470
- Gold now: 408
- HTTP: 72 alive / 52 gold
- HTTPS: 40 alive / 22 gold
- SOCKS4: 174 alive / 163 gold
- SOCKS5: 184 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47112
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
