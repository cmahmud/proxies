# SyndProxy validated proxy pool

## Current pool

- Alive now: 390
- Gold now: 319
- HTTP: 88 alive / 64 gold
- HTTPS: 33 alive / 21 gold
- SOCKS4: 122 alive / 104 gold
- SOCKS5: 147 alive / 130 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49519
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
