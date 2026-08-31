# SyndProxy validated proxy pool

## Current pool

- Alive now: 564
- Gold now: 435
- HTTP: 116 alive / 74 gold
- HTTPS: 68 alive / 26 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 204 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45556
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
