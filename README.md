# SyndProxy validated proxy pool

## Current pool

- Alive now: 642
- Gold now: 474
- HTTP: 151 alive / 98 gold
- HTTPS: 116 alive / 37 gold
- SOCKS4: 181 alive / 163 gold
- SOCKS5: 194 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45248
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
