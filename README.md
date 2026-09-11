# SyndProxy validated proxy pool

## Current pool

- Alive now: 463
- Gold now: 378
- HTTP: 84 alive / 65 gold
- HTTPS: 44 alive / 24 gold
- SOCKS4: 146 alive / 119 gold
- SOCKS5: 189 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48733
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
