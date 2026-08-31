# SyndProxy validated proxy pool

## Current pool

- Alive now: 599
- Gold now: 459
- HTTP: 119 alive / 91 gold
- HTTPS: 118 alive / 36 gold
- SOCKS4: 172 alive / 163 gold
- SOCKS5: 190 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45669
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
