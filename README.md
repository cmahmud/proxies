# SyndProxy validated proxy pool

## Current pool

- Alive now: 682
- Gold now: 479
- HTTP: 167 alive / 101 gold
- HTTPS: 120 alive / 39 gold
- SOCKS4: 179 alive / 163 gold
- SOCKS5: 216 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45254
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
