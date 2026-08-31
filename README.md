# SyndProxy validated proxy pool

## Current pool

- Alive now: 582
- Gold now: 456
- HTTP: 116 alive / 89 gold
- HTTPS: 104 alive / 34 gold
- SOCKS4: 170 alive / 163 gold
- SOCKS5: 192 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45662
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
