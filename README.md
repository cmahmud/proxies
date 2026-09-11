# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 385
- HTTP: 92 alive / 64 gold
- HTTPS: 42 alive / 18 gold
- SOCKS4: 168 alive / 130 gold
- SOCKS5: 190 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48753
- Ever gold: 1565

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
