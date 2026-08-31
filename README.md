# SyndProxy validated proxy pool

## Current pool

- Alive now: 685
- Gold now: 466
- HTTP: 150 alive / 91 gold
- HTTPS: 132 alive / 38 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 230 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45271
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
