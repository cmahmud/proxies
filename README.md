# SyndProxy validated proxy pool

## Current pool

- Alive now: 682
- Gold now: 472
- HTTP: 170 alive / 97 gold
- HTTPS: 116 alive / 38 gold
- SOCKS4: 176 alive / 159 gold
- SOCKS5: 220 alive / 178 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45307
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
