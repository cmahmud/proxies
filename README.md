# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 374
- HTTP: 83 alive / 52 gold
- HTTPS: 53 alive / 12 gold
- SOCKS4: 169 alive / 153 gold
- SOCKS5: 182 alive / 157 gold

## Historical pool

- Discovered: 173755
- Ever alive: 33040
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
