# SyndProxy validated proxy pool

## Current pool

- Alive now: 642
- Gold now: 465
- HTTP: 121 alive / 91 gold
- HTTPS: 122 alive / 36 gold
- SOCKS4: 174 alive / 163 gold
- SOCKS5: 225 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45726
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
