# SyndProxy validated proxy pool

## Current pool

- Alive now: 669
- Gold now: 462
- HTTP: 141 alive / 89 gold
- HTTPS: 133 alive / 35 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 224 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45269
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
