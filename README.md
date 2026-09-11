# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 392
- HTTP: 95 alive / 66 gold
- HTTPS: 38 alive / 22 gold
- SOCKS4: 166 alive / 131 gold
- SOCKS5: 192 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48762
- Ever gold: 1565

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
