# SyndProxy validated proxy pool

## Current pool

- Alive now: 576
- Gold now: 424
- HTTP: 120 alive / 68 gold
- HTTPS: 64 alive / 23 gold
- SOCKS4: 184 alive / 161 gold
- SOCKS5: 208 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45525
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
