# SyndProxy validated proxy pool

## Current pool

- Alive now: 611
- Gold now: 470
- HTTP: 134 alive / 94 gold
- HTTPS: 114 alive / 38 gold
- SOCKS4: 173 alive / 164 gold
- SOCKS5: 190 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46890
- Ever gold: 1456

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
