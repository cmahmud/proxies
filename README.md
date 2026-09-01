# SyndProxy validated proxy pool

## Current pool

- Alive now: 603
- Gold now: 470
- HTTP: 128 alive / 91 gold
- HTTPS: 106 alive / 42 gold
- SOCKS4: 178 alive / 163 gold
- SOCKS5: 191 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46965
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
