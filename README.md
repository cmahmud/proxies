# SyndProxy validated proxy pool

## Current pool

- Alive now: 624
- Gold now: 466
- HTTP: 137 alive / 89 gold
- HTTPS: 116 alive / 40 gold
- SOCKS4: 181 alive / 163 gold
- SOCKS5: 190 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46969
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
