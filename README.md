# SyndProxy validated proxy pool

## Current pool

- Alive now: 627
- Gold now: 460
- HTTP: 134 alive / 91 gold
- HTTPS: 130 alive / 33 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 187 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46681
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
