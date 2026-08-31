# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 452
- HTTP: 123 alive / 86 gold
- HTTPS: 92 alive / 35 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 188 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45650
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
