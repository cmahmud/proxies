# SyndProxy validated proxy pool

## Current pool

- Alive now: 633
- Gold now: 468
- HTTP: 146 alive / 91 gold
- HTTPS: 116 alive / 40 gold
- SOCKS4: 182 alive / 163 gold
- SOCKS5: 189 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46968
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
