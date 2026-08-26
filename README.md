# SyndProxy validated proxy pool

## Current pool

- Alive now: 660
- Gold now: 410
- HTTP: 148 alive / 74 gold
- HTTPS: 160 alive / 20 gold
- SOCKS4: 164 alive / 155 gold
- SOCKS5: 188 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40259
- Ever gold: 1308

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
