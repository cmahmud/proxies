# SyndProxy validated proxy pool

## Current pool

- Alive now: 465
- Gold now: 398
- HTTP: 75 alive / 58 gold
- HTTPS: 53 alive / 19 gold
- SOCKS4: 164 alive / 158 gold
- SOCKS5: 173 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42823
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
