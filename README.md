# SyndProxy validated proxy pool

## Current pool

- Alive now: 636
- Gold now: 467
- HTTP: 143 alive / 93 gold
- HTTPS: 128 alive / 39 gold
- SOCKS4: 174 alive / 163 gold
- SOCKS5: 191 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46912
- Ever gold: 1457

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
