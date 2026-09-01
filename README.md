# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 417
- HTTP: 80 alive / 63 gold
- HTTPS: 51 alive / 20 gold
- SOCKS4: 190 alive / 163 gold
- SOCKS5: 181 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47119
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
