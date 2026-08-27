# SyndProxy validated proxy pool

## Current pool

- Alive now: 559
- Gold now: 419
- HTTP: 97 alive / 68 gold
- HTTPS: 106 alive / 22 gold
- SOCKS4: 170 alive / 164 gold
- SOCKS5: 186 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41462
- Ever gold: 1332

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
