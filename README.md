# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 443
- HTTP: 119 alive / 78 gold
- HTTPS: 66 alive / 32 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 196 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45558
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
