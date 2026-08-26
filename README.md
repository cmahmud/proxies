# SyndProxy validated proxy pool

## Current pool

- Alive now: 635
- Gold now: 394
- HTTP: 159 alive / 67 gold
- HTTPS: 120 alive / 22 gold
- SOCKS4: 165 alive / 150 gold
- SOCKS5: 191 alive / 155 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39523
- Ever gold: 1299

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
