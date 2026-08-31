# SyndProxy validated proxy pool

## Current pool

- Alive now: 643
- Gold now: 445
- HTTP: 149 alive / 78 gold
- HTTPS: 105 alive / 33 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 221 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45441
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
