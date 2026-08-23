# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 366
- HTTP: 105 alive / 46 gold
- HTTPS: 31 alive / 11 gold
- SOCKS4: 187 alive / 153 gold
- SOCKS5: 189 alive / 156 gold

## Historical pool

- Discovered: 173755
- Ever alive: 33025
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
