# SyndProxy validated proxy pool

## Current pool

- Alive now: 788
- Gold now: 197
- HTTP: 322 alive / 36 gold
- HTTPS: 53 alive / 6 gold
- SOCKS4: 212 alive / 67 gold
- SOCKS5: 201 alive / 88 gold

## Historical pool

- Discovered: 170566
- Ever alive: 32772
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
