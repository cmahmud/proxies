# SyndProxy private pool

## Current pool

- Alive now: 717
- Gold now: 400
- HTTP: 189 alive / 83 gold
- HTTPS: 104 alive / 15 gold
- SOCKS4: 207 alive / 149 gold
- SOCKS5: 217 alive / 153 gold

## Historical pool

- Discovered: 155785
- Ever alive: 29301
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
