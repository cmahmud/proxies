# SyndProxy validated proxy pool

## Current pool

- Alive now: 634
- Gold now: 466
- HTTP: 135 alive / 92 gold
- HTTPS: 117 alive / 35 gold
- SOCKS4: 171 alive / 163 gold
- SOCKS5: 211 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46427
- Ever gold: 1444

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
