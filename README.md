# SyndProxy validated proxy pool

## Current pool

- Alive now: 676
- Gold now: 474
- HTTP: 163 alive / 99 gold
- HTTPS: 122 alive / 37 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 214 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45253
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
