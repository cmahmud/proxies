# SyndProxy validated proxy pool

## Current pool

- Alive now: 643
- Gold now: 393
- HTTP: 160 alive / 67 gold
- HTTPS: 119 alive / 22 gold
- SOCKS4: 169 alive / 150 gold
- SOCKS5: 195 alive / 154 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39543
- Ever gold: 1299

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
