# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 429
- HTTP: 111 alive / 81 gold
- HTTPS: 60 alive / 29 gold
- SOCKS4: 158 alive / 155 gold
- SOCKS5: 176 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43656
- Ever gold: 1376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
