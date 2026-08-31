# SyndProxy validated proxy pool

## Current pool

- Alive now: 662
- Gold now: 463
- HTTP: 133 alive / 92 gold
- HTTPS: 136 alive / 29 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 220 alive / 179 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45991
- Ever gold: 1438

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
