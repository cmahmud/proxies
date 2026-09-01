# SyndProxy validated proxy pool

## Current pool

- Alive now: 624
- Gold now: 454
- HTTP: 128 alive / 85 gold
- HTTPS: 130 alive / 34 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 188 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46852
- Ever gold: 1452

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
