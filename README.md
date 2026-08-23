# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 342
- HTTP: 117 alive / 40 gold
- HTTPS: 48 alive / 8 gold
- SOCKS4: 175 alive / 153 gold
- SOCKS5: 189 alive / 141 gold

## Historical pool

- Discovered: 171565
- Ever alive: 32889
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
