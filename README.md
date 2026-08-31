# SyndProxy validated proxy pool

## Current pool

- Alive now: 708
- Gold now: 469
- HTTP: 162 alive / 94 gold
- HTTPS: 144 alive / 36 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 228 alive / 178 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45266
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
