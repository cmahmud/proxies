# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 383
- HTTP: 91 alive / 64 gold
- HTTPS: 44 alive / 18 gold
- SOCKS4: 170 alive / 129 gold
- SOCKS5: 191 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48753
- Ever gold: 1565

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
