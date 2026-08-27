# SyndProxy validated proxy pool

## Current pool

- Alive now: 649
- Gold now: 410
- HTTP: 127 alive / 72 gold
- HTTPS: 148 alive / 19 gold
- SOCKS4: 178 alive / 155 gold
- SOCKS5: 196 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40525
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
