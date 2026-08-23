# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 375
- HTTP: 85 alive / 52 gold
- HTTPS: 54 alive / 13 gold
- SOCKS4: 169 alive / 153 gold
- SOCKS5: 182 alive / 157 gold

## Historical pool

- Discovered: 173755
- Ever alive: 33040
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
