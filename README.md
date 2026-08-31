# SyndProxy validated proxy pool

## Current pool

- Alive now: 652
- Gold now: 462
- HTTP: 117 alive / 91 gold
- HTTPS: 103 alive / 36 gold
- SOCKS4: 192 alive / 163 gold
- SOCKS5: 240 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45690
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
