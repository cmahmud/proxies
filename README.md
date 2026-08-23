# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 365
- HTTP: 109 alive / 45 gold
- HTTPS: 27 alive / 11 gold
- SOCKS4: 189 alive / 153 gold
- SOCKS5: 185 alive / 156 gold

## Historical pool

- Discovered: 173755
- Ever alive: 33025
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
