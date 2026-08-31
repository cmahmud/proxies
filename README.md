# SyndProxy validated proxy pool

## Current pool

- Alive now: 684
- Gold now: 453
- HTTP: 150 alive / 89 gold
- HTTPS: 116 alive / 31 gold
- SOCKS4: 178 alive / 160 gold
- SOCKS5: 240 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45320
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
