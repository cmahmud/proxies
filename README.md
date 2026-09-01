# SyndProxy validated proxy pool

## Current pool

- Alive now: 628
- Gold now: 457
- HTTP: 135 alive / 87 gold
- HTTPS: 132 alive / 35 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 189 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46860
- Ever gold: 1452

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
