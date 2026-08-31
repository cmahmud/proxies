# SyndProxy validated proxy pool

## Current pool

- Alive now: 650
- Gold now: 479
- HTTP: 158 alive / 103 gold
- HTTPS: 123 alive / 39 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 192 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45247
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
