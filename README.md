# SyndProxy validated proxy pool

## Current pool

- Alive now: 630
- Gold now: 392
- HTTP: 126 alive / 68 gold
- HTTPS: 146 alive / 23 gold
- SOCKS4: 170 alive / 146 gold
- SOCKS5: 188 alive / 155 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39608
- Ever gold: 1299

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
