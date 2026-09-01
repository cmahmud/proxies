# SyndProxy validated proxy pool

## Current pool

- Alive now: 577
- Gold now: 438
- HTTP: 104 alive / 73 gold
- HTTPS: 112 alive / 29 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 192 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47345
- Ever gold: 1466

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
