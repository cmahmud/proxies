# SyndProxy validated proxy pool

## Current pool

- Alive now: 466
- Gold now: 394
- HTTP: 68 alive / 60 gold
- HTTPS: 52 alive / 17 gold
- SOCKS4: 174 alive / 154 gold
- SOCKS5: 172 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42809
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
