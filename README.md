# SyndProxy validated proxy pool

## Current pool

- Alive now: 699
- Gold now: 455
- HTTP: 160 alive / 90 gold
- HTTPS: 125 alive / 30 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 240 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45317
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
