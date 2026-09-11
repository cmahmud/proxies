# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 387
- HTTP: 95 alive / 65 gold
- HTTPS: 42 alive / 18 gold
- SOCKS4: 166 alive / 130 gold
- SOCKS5: 189 alive / 174 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48753
- Ever gold: 1565

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
