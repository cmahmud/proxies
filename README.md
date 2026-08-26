# SyndProxy validated proxy pool

## Current pool

- Alive now: 651
- Gold now: 393
- HTTP: 159 alive / 67 gold
- HTTPS: 125 alive / 21 gold
- SOCKS4: 172 alive / 150 gold
- SOCKS5: 195 alive / 155 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39567
- Ever gold: 1299

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
