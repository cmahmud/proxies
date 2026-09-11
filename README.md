# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 389
- HTTP: 96 alive / 66 gold
- HTTPS: 42 alive / 20 gold
- SOCKS4: 169 alive / 130 gold
- SOCKS5: 191 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48760
- Ever gold: 1565

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
