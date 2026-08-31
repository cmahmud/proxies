# SyndProxy validated proxy pool

## Current pool

- Alive now: 650
- Gold now: 463
- HTTP: 116 alive / 91 gold
- HTTPS: 100 alive / 37 gold
- SOCKS4: 192 alive / 163 gold
- SOCKS5: 242 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45690
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
