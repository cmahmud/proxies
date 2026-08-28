# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 400
- HTTP: 86 alive / 57 gold
- HTTPS: 53 alive / 14 gold
- SOCKS4: 171 alive / 164 gold
- SOCKS5: 177 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42834
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
