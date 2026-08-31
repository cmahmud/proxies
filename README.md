# SyndProxy validated proxy pool

## Current pool

- Alive now: 695
- Gold now: 465
- HTTP: 155 alive / 93 gold
- HTTPS: 135 alive / 34 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 232 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45268
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
