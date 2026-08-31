# SyndProxy validated proxy pool

## Current pool

- Alive now: 628
- Gold now: 479
- HTTP: 138 alive / 101 gold
- HTTPS: 117 alive / 43 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 201 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45060
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
