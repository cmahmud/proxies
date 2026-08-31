# SyndProxy validated proxy pool

## Current pool

- Alive now: 601
- Gold now: 450
- HTTP: 138 alive / 83 gold
- HTTPS: 95 alive / 36 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 195 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45584
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
