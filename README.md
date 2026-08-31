# SyndProxy validated proxy pool

## Current pool

- Alive now: 572
- Gold now: 457
- HTTP: 115 alive / 90 gold
- HTTPS: 97 alive / 34 gold
- SOCKS4: 168 alive / 163 gold
- SOCKS5: 192 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45662
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
