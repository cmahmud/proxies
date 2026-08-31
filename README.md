# SyndProxy validated proxy pool

## Current pool

- Alive now: 696
- Gold now: 470
- HTTP: 176 alive / 93 gold
- HTTPS: 122 alive / 38 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 226 alive / 179 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45286
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
