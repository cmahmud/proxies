# SyndProxy validated proxy pool

## Current pool

- Alive now: 709
- Gold now: 467
- HTTP: 161 alive / 93 gold
- HTTPS: 146 alive / 36 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 229 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45267
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
