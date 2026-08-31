# SyndProxy validated proxy pool

## Current pool

- Alive now: 673
- Gold now: 468
- HTTP: 164 alive / 97 gold
- HTTPS: 113 alive / 37 gold
- SOCKS4: 173 alive / 159 gold
- SOCKS5: 223 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45306
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
