# SyndProxy validated proxy pool

## Current pool

- Alive now: 684
- Gold now: 463
- HTTP: 169 alive / 95 gold
- HTTPS: 115 alive / 35 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 228 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45305
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
