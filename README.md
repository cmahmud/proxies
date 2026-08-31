# SyndProxy validated proxy pool

## Current pool

- Alive now: 683
- Gold now: 460
- HTTP: 125 alive / 90 gold
- HTTPS: 146 alive / 34 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 234 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45822
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
