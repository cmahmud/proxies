# SyndProxy validated proxy pool

## Current pool

- Alive now: 623
- Gold now: 454
- HTTP: 135 alive / 85 gold
- HTTPS: 131 alive / 33 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 189 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46817
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
