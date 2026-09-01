# SyndProxy validated proxy pool

## Current pool

- Alive now: 624
- Gold now: 467
- HTTP: 146 alive / 93 gold
- HTTPS: 119 alive / 40 gold
- SOCKS4: 171 alive / 163 gold
- SOCKS5: 188 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46907
- Ever gold: 1457

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
