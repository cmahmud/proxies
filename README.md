# SyndProxy validated proxy pool

## Current pool

- Alive now: 585
- Gold now: 425
- HTTP: 125 alive / 68 gold
- HTTPS: 65 alive / 24 gold
- SOCKS4: 185 alive / 161 gold
- SOCKS5: 210 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45525
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
