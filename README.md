# SyndProxy validated proxy pool

## Current pool

- Alive now: 384
- Gold now: 307
- HTTP: 104 alive / 79 gold
- HTTPS: 48 alive / 22 gold
- SOCKS4: 80 alive / 71 gold
- SOCKS5: 152 alive / 135 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47927
- Ever gold: 1505

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
