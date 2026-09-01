# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 463
- HTTP: 141 alive / 93 gold
- HTTPS: 121 alive / 36 gold
- SOCKS4: 174 alive / 163 gold
- SOCKS5: 193 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46912
- Ever gold: 1457

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
