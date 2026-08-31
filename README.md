# SyndProxy validated proxy pool

## Current pool

- Alive now: 682
- Gold now: 465
- HTTP: 134 alive / 90 gold
- HTTPS: 144 alive / 37 gold
- SOCKS4: 174 alive / 163 gold
- SOCKS5: 230 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45884
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
