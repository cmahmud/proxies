# SyndProxy validated proxy pool

## Current pool

- Alive now: 570
- Gold now: 401
- HTTP: 100 alive / 62 gold
- HTTPS: 104 alive / 14 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 191 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41432
- Ever gold: 1328

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
