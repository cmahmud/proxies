# SyndProxy validated proxy pool

## Current pool

- Alive now: 683
- Gold now: 462
- HTTP: 127 alive / 91 gold
- HTTPS: 146 alive / 34 gold
- SOCKS4: 176 alive / 163 gold
- SOCKS5: 234 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45806
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
