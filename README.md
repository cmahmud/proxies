# SyndProxy validated proxy pool

## Current pool

- Alive now: 475
- Gold now: 402
- HTTP: 73 alive / 55 gold
- HTTPS: 61 alive / 24 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 173 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42784
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
