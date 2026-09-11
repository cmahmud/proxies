# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 298
- HTTP: 165 alive / 74 gold
- HTTPS: 159 alive / 36 gold
- SOCKS4: 53 alive / 52 gold
- SOCKS5: 138 alive / 136 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48484
- Ever gold: 1542

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
