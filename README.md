# SyndProxy validated proxy pool

## Current pool

- Alive now: 581
- Gold now: 422
- HTTP: 126 alive / 65 gold
- HTTPS: 68 alive / 25 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 208 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45526
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
