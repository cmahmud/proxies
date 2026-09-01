# SyndProxy validated proxy pool

## Current pool

- Alive now: 643
- Gold now: 462
- HTTP: 149 alive / 92 gold
- HTTPS: 126 alive / 35 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 190 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46866
- Ever gold: 1452

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
