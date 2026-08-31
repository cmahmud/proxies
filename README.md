# SyndProxy validated proxy pool

## Current pool

- Alive now: 638
- Gold now: 445
- HTTP: 146 alive / 78 gold
- HTTPS: 100 alive / 33 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 224 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45441
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
