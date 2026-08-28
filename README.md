# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 400
- HTTP: 89 alive / 55 gold
- HTTPS: 52 alive / 15 gold
- SOCKS4: 175 alive / 164 gold
- SOCKS5: 175 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42834
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
