# SyndProxy validated proxy pool

## Current pool

- Alive now: 724
- Gold now: 472
- HTTP: 175 alive / 93 gold
- HTTPS: 128 alive / 39 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 247 alive / 179 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45284
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
