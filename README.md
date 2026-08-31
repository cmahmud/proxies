# SyndProxy validated proxy pool

## Current pool

- Alive now: 572
- Gold now: 436
- HTTP: 125 alive / 75 gold
- HTTPS: 72 alive / 26 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 198 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45548
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
