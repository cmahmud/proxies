# SyndProxy validated proxy pool

## Current pool

- Alive now: 639
- Gold now: 461
- HTTP: 136 alive / 90 gold
- HTTPS: 138 alive / 35 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 189 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46687
- Ever gold: 1446

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
