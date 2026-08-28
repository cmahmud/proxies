# SyndProxy validated proxy pool

## Current pool

- Alive now: 473
- Gold now: 400
- HTTP: 82 alive / 59 gold
- HTTPS: 43 alive / 14 gold
- SOCKS4: 172 alive / 163 gold
- SOCKS5: 176 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42831
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
