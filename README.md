# SyndProxy validated proxy pool

## Current pool

- Alive now: 616
- Gold now: 460
- HTTP: 123 alive / 92 gold
- HTTPS: 133 alive / 34 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 188 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46712
- Ever gold: 1447

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
