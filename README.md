# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 460
- HTTP: 133 alive / 89 gold
- HTTPS: 132 alive / 33 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 187 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46646
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
